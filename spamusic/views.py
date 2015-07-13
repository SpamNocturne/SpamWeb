from .models import CredentialsYoutubeModel
from SpamWeb import settings
from . import functions as f

from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest
from oauth2client import xsrfutil
from oauth2client.django_orm import Storage




# VIEWS

@login_required
def OAuthReturn(request):
    master = f.get_youtube_master()
    if not xsrfutil.validate_token(settings.SECRET_KEY.encode('latin1'), request.REQUEST['state'].encode('latin1'), master):
        return HttpResponseBadRequest()
    credential = f.get_flow.step2_exchange(request.REQUEST)
    storage = Storage(CredentialsYoutubeModel, 'id', master, 'credential')
    storage.put(credential)
    return redirect(reverse('spamusic:index'))


@login_required
def index(request):
    # vérifications d'accès à l'API
    master = f.get_youtube_master()
    check = f.check_youtube_master(request=request, master=master)
    if check['status'] is False:
        return check['value']
    check = f.check_api_token(request=request, master=master)
    if check['status'] is False:
        return check['value']
    else:
        credential = check['value']

    if request.user.is_superuser:
        message = "Vous êtes un admin !"
    else:
        message = "Vous n'etes pas un admin !"
    title = "Compte SpamWeb Connecté !"

    youtube = f.build_youtube(credential)

    playlist_list = f.playlist_list(youtube)

    yt_message = ""
    context = {
        'title': title,
        'message': message,
        'yt_message': yt_message,
        'playlist_list': playlist_list,
    }
    return render(request, 'spamusic/index.html', context)


