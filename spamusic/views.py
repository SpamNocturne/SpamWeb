from .models import CredentialsYoutubeModel
from SpamWeb import settings
from . import functions as f

from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from oauth2client import xsrfutil
from oauth2client.django_orm import Storage




# VIEWS

@login_required
def OAuthReturn(request):
    master = f.get_youtube_master()
    if not xsrfutil.validate_token(settings.SECRET_KEY.encode('latin1'), request.GET['state'].encode('latin1'),
                                   master):
        return HttpResponseBadRequest()
    credential = f.get_flow().step2_exchange(request.GET)
    storage = Storage(CredentialsYoutubeModel, 'id', master, 'credential')
    storage.put(credential)
    return redirect('spamusic:index')


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
        admin = "Vous êtes un admin !"
    else:
        admin = "Vous n'etes pas un admin !"

    youtube = f.build_youtube(credential)

    playlist_list = f.playlist_list(youtube)
    '''
    playlist_list = {
        "items": [
            {
                "id": "PLFp2-gAWp2eVjZYkT502Xd0tMHFD0YjP9",
                "snippet": {
                    "publishedAt": "2015-07-10T23:57:32.000Z",
                    "channelId": "UC8iUi9DiP_Nr6uAuo7W74XQ",
                    "title": "Test spamweb",
                    "description": "",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/JhGkt6PQQ8E/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/JhGkt6PQQ8E/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/JhGkt6PQQ8E/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/JhGkt6PQQ8E/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        }
                    },
                    "channelTitle": "SpamWeb",
                    "localized": {
                        "title": "Test spamweb",
                        "description": ""
                    }
                },
                "contentDetails": {
                    "itemCount": 4
                }
            }
        ]
    }
    '''
    yt_message = ""
    context = {
        'admin': admin,
        'yt_message': yt_message,
        'playlist_list': playlist_list,
    }
    return render(request, 'spamusic/index.html', context)
