import os
import logging
import httplib2

from apiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from .models import CredentialsModel
from SpamWeb import settings
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

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

CLIENT_SECRETS_FILE = "spamusic/config/client_secrets.json"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
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
# This OAuth 2.0 access scope allows for read-only access to the authenticated
# user's account, but not other types of account access.
YOUTUBE_ALL_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
FLOW = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    message=MISSING_CLIENT_SECRETS_MESSAGE,
    scope=YOUTUBE_ALL_SCOPE,
    redirect_uri='http://127.0.0.1:8000/spamusic/OAuthReturn/')
#TODO REDIRECT URI PAS PROPRE

@login_required()
def OAuthAuthentification(request):

    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    print("coucou")

    if credential is None or credential.invalid == True:
        print("if")
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                     request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return redirect(authorize_url)
    else:
        print("else")
        http = httplib2.Http()
        http = credential.authorize(http)
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=http)
        '''
        activities = service.activities()
        activitylist = activities.list(collection='public',
                                       userId='me').execute()
        logging.info(activitylist)
        '''
        return render_to_response('spamusic/index.html', {
                    'message': "YES ! ",
                    })
@login_required
def OAuthReturn(request):
    if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'],
                                 request.user):
        return  HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.REQUEST)
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    storage.put(credential)
    return redirect(reverse('spamusic:OAuthAuthentification'))

@login_required
def index(request):
    '''
    youtube = init_youtube()
    # This code creates a new, private playlist in the authorized user's channel.
    playlists_insert_response = youtube.playlists().insert(
      part="snippet,status",
      body=dict(
        snippet=dict(
          title="Test Playlist",
          description="A private playlist created with the YouTube API v3"
        ),
        status=dict(
          privacyStatus="private"
        )
      )
    ).execute()
    #latest_question_list = Idee.objects.order_by('-pub_date')
    #context = {'idee_list': latest_question_list}
    context = {"message": "New playlist id: %s" % playlists_insert_response["id"]}
    '''
    context = {}
    return render(request, 'spamusic/index.html', context)
