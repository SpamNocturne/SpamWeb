# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google Developers Console at
# https://console.developers.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
import os
import httplib2
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from googleapiclient.discovery import build
from django.shortcuts import render_to_response
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage
from SpamWeb import settings
from spamusic.models import CredentialsYoutubeModel

CLIENT_SECRETS_FILE = "spamusic/config/client_secrets.json"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))
# This OAuth 2.0 access scope allows for full access to the authenticated
# user's account, but not other types of account access. (pas de service accounts :c )
YOUTUBE_ALL_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
FLOW = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                               message=MISSING_CLIENT_SECRETS_MESSAGE,
                               scope=YOUTUBE_ALL_SCOPE,
                               #  TODO REDIRECT URI PAS PROPRE
                               redirect_uri='http://127.0.0.1:8000/spamusic/OAuthReturn/')


# Propriétaire de la playlist collaborative
YOUTUBE_MASTER_USERNAME = "spamadmin"


# Connection functions
def build_youtube(credential):
    http = httplib2.Http()
    http = credential.authorize(http)
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=http)


# retourne le user propriétaire de la playlist, s'il n'est pas en base, retourne None
def get_youtube_master():
    master = User.objects.filter(username=YOUTUBE_MASTER_USERNAME)
    if master:
        # si le master existe, il ne peut y en avoir qu'un et UN SEUL. TRUE MASTEEEEEEER !
        # Non plus serieusement, c'est parce que l'username est unique :D
        if master[0]:
            return master[0]
    return None


def get_flow():
    return FLOW


# vérifie le retour de la fonction get_youtube_master, et en cas d'erreur genere les vues d'erreur
# La valeur de retour est un dictionnaire contenant :
#   - 'status' Booleen (code retour)
#   - 'value' la valeur retournée (potentiellement une response, ou un objet attendu)
def check_youtube_master(request, master):
    # s'il n'y a pas de youtube master, il en faut un !
    if master is None:
        # si l'utilisateur connecté est un admin, il doit créer le maitre
        if request.user.is_superuser:
            context = {
                'title': "Où est le maître ?",
                'message': "Le user %s n'a pas été trouvé dans la base, veuillez le créer. "
                           "Il est nôtre maître." % YOUTUBE_MASTER_USERNAME
            }
            return {'status': False, 'value': render_to_response('spamusic/message.html', context)}
        else:
            context = {
                'title': "Oups ...",
                'message': "Le compte youtube de SpamWeb n'a pas été associé à l'application. "
                           "Veuillez contacter un administrateur"
            }
            return {'status': False, 'value': render_to_response('spamusic/message.html', context)}
    return {'status': True, 'value': None}


# vérifie que les autorisation sont présentes et à jour, et en cas d'erreur genere les vues d'erreur
# La valeur de retour est un dictionnaire contenant :
#   - 'status' Booleen (code retour)
#   - 'value' la valeur retournée (potentiellement une response, ou un objet attendu)
@login_required()
def check_api_token(request, master):
    storage = Storage(CredentialsYoutubeModel, 'id', master, 'credential')
    credential = storage.get()
    # Si les autorisation n'ont pas été données où sont devenue invalides
    if credential is None or credential.invalid is True:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, master)
        authorize_url = FLOW.step1_get_authorize_url()

        # si l'utilisateur connecté est un admin, il doit mettre à jour les autorisations
        if request.user.is_superuser:
            context = {
                'title': "On a besoin de vous !",
                'message': "Bienvenue ! Comme tu peux le voir c'est la guerre ici, tout ne marche pas comme prévu ... "
                           "Mais heureusement que tu es là ! "
                           "Le président ne veut plus nous subventionner "
                           "(c'est plutôt son compte youtube qui ne nous est plus accessible ...) ! "
                           "Convaincs-le, et récupère nous ses autorisations ! Son nom est : SpamWeb. "
                           "Tu as carte blanche "
                           "(tu pourrais par exemple te connecter à son compte google avant de continuer ...) ! "
                           "Allez juste un dernier conseil : "
                           "tu devrais essayer spamweb.dev@gmail.com / spamnocturne. Bonne chance !",
                'url_for_admin': authorize_url
            }
            return {'status': False, 'value': render_to_response('spamusic/message.html', context)}
        else:
            context = {
                'title': "Oups ...",
                'message': "Le compte youtube de SpamWeb a besoin de mettre ses autorisations à jour. "
                           "Veuillez contacter un administrateur"
            }
            return {'status': False, 'value': render_to_response('spamusic/message.html', context)}
    return {'status': True, 'value': credential}


# API SHORTCUTS
def playlist_create(youtube, name):
    kwargs = {
        'part': 'id,snippet,contentDetails,status',
        'body': {
            'snippet': {
                'title': name,
            },
            'status': {
                'privacyStatus': 'public',
            },
        },
        'fields': 'contentDetails,id,snippet',
    }
    return youtube.playlists().insert(**kwargs).execute()


def playlist_list(youtube):
    kwargs = {
        'part': 'id,contentDetails,snippet',
        'maxResults': 50,
        'mine': True,
        'fields': 'items(contentDetails,id,snippet)',
    }
    return youtube.playlists().list(**kwargs).execute()


def playlist_details(youtube, playlist_id):
    kwargs = {
        'part': 'contentDetails,id,player,snippet',
        'id': playlist_id,
        'fields': 'items(contentDetails,id,player,snippet)',
    }
    return youtube.playlists().list(**kwargs).execute()

def playlist_items_list_all(youtube, playlist_id):
    kwargs = {
        'part': 'snippet,id',
        'maxResults': 50,
        'playlistId': playlist_id,
        'fields': 'items(id,snippet)',
    }
    playlistitems_list_request = youtube.playlistItems().list(**kwargs)

    playlistitems_list_response = playlistitems_list_request.execute()
    playlistitems_list_request = youtube.playlistItems().list_next(
        playlistitems_list_request,
        playlistitems_list_response
    )

    # on récupère aussi les pages suivantes
    while playlistitems_list_request:
        playlistitems_list_response_add = playlistitems_list_request.execute()
        # concatenation des resultats
        playlistitems_list_response["items"] += playlistitems_list_response_add["items"]
        # playlistitems_list_response["items"].extends(playlistitems_list_response_add["items"])

    return playlistitems_list_response
