
'''
    AJAX SPAMUSIC
'''



# Va chercher toutes les playlistes du master et les rend en template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from home.log import add_log
from . import functions as f


@login_required()
def ajax_ajouter_playlist(request):
    name = request.POST['name']

    master = f.get_youtube_master()
    check = f.check_youtube_master(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    check = f.check_api_token(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    else:
        credential = check['value']

    youtube = f.build_youtube(credential)
    playlist = f.playlist_create(youtube=youtube, name=name)
    add_log(text="%s a créé une nouvelle playlist : %s" % (request.user.username, name),
            app="spamusic",
            log_type="spamusic_add_playlist",
            user=request.user)
    context = {'playlist': playlist}
    return render(request, 'spamusic/control-sidebar-playlist.html', context)


# récupère les élément d'une playlist et les rend l'onglet video les contenants
@login_required()
def ajax_playlistitems(request):
    playlist_id = request.POST['playlist_id']
    master = f.get_youtube_master()
    check = f.check_youtube_master(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    check = f.check_api_token(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    else:
        credential = check['value']

    youtube = f.build_youtube(credential)
    playlist_items = f.playlist_items_list_all(youtube=youtube, playlist_id=playlist_id)
    '''
    playlist_items = {
        "items": [
            {
                "id": "PL2qvtSnCzogLZMGwm6eJnnMmGXmABvK__Y7ElRBdXPy4",
                "snippet": {
                    "publishedAt": "2015-07-13T17:35:22.000Z",
                    "channelId": "UC8iUi9DiP_Nr6uAuo7W74XQ",
                    "title": "Uppermost - Flashback",
                    "description": "Uppermost's incredible new album 'One' is out now! I highly recommend purchasing it.\nhttp://btprt.dj/1rTxUaX\nhttp://shop.uppwind.com/product.php?id_product=11\n\nUppermost:\nhttp://soundcloud.com/uppermost/\nhttp://www.uppwind.com/\nhttp://www.facebook.com/uppermost\nhttps://twitter.com/uppermostmusic\n\nSheepy twitter\nhttps://twitter.com/MrSuicideSheep\n\nPicture:\nhttp://www.flickr.com/photos/makayla_rogers/7483979652/\n\nMrSuicideSheep t-shirts!!!\nhttp://bit.ly/1813nN5",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/i78U3VEAwK8/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/i78U3VEAwK8/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/i78U3VEAwK8/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/i78U3VEAwK8/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        },
                        "maxres": {
                            "url": "https://i.ytimg.com/vi/i78U3VEAwK8/maxresdefault.jpg",
                            "width": 1280,
                            "height": 720
                        }
                    },
                    "channelTitle": "SpamWeb",
                    "playlistId": "PLFp2-gAWp2eVjZYkT502Xd0tMHFD0YjP9",
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": "i78U3VEAwK8"
                    }
                }
            },
            {
                "id": "PL2qvtSnCzogLZMGwm6eJnnCB4xk0TuXWrZJp7_JDMGRg",
                "snippet": {
                    "publishedAt": "2015-07-13T17:37:28.000Z",
                    "channelId": "UC8iUi9DiP_Nr6uAuo7W74XQ",
                    "title": "ODESZA - Don't Stop",
                    "description": "I'll let the music do the talking :)\nODESZA released their first album for free! Grab it here:\nhttp://www.mediafire.com/?25qk5hd4d02ofj6\n\nMake sure to give them your love.\nhttp://soundcloud.com/odesza\nhttps://www.facebook.com/pages/Odesza/428904283808020\n\nPicture:\nhttp://rhads.deviantart.com/art/Wallpaper-Land-of-the-Wind-327743415?offset=20\n\nFaceboob:\nhttp://www.facebook.com/MrSuicideSheep",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/BFW_Mxefvig/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/BFW_Mxefvig/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/BFW_Mxefvig/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/BFW_Mxefvig/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        },
                        "maxres": {
                            "url": "https://i.ytimg.com/vi/BFW_Mxefvig/maxresdefault.jpg",
                            "width": 1280,
                            "height": 720
                        }
                    },
                    "channelTitle": "SpamWeb",
                    "playlistId": "PLFp2-gAWp2eVjZYkT502Xd0tMHFD0YjP9",
                    "position": 1,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": "BFW_Mxefvig"
                    }
                }
            },
            {
                "id": "PL2qvtSnCzogLZMGwm6eJnnNJv9idCMGRiDy6bRe4I_9w",
                "snippet": {
                    "publishedAt": "2015-07-11T08:38:21.000Z",
                    "channelId": "UC8iUi9DiP_Nr6uAuo7W74XQ",
                    "title": "Listenbee - Save Me (Tez Cadey Remix)",
                    "description": "This remix is completely addicting! I can't help but move along to it.\nListen to the original... http://goo.gl/5ToJ2M\n\nTez Cadey\nhttps://soundcloud.com/tezcadey\nhttps://www.facebook.com/pages/Tez-Cadey/125292844188815?ref=ts\nhttps://twitter.com/TezCadey\n\nListenbee\nhttps://soundcloud.com/listenbee\nhttps://www.facebook.com/listenbeemusic\nhttps://twitter.com/listenbeemusic\nhttp://instagram.com/listenbeemusic\n\nReleased by Lokal Legend\nhttps://www.facebook.com/lokallegend\nhttps://twitter.com/lokallegend\nhttp://instagram.com/lokallegend\n\nPicture by Marat Safin\nhttps://flic.kr/p/fZ2zZn\nhttps://www.facebook.com/maratsafinphotography\n\nFacebooobs\nhttps://www.facebook.com/MrSuicideSheep\n\nFollow on Soundcloud\nhttps://soundcloud.com/mrsuicidesheep\n\nFollow on Twitter\nhttps://twitter.com/mrsuicidesheep\n\nSheepy t-shirts!\nhttp://bit.ly/Sheepytees\n\nSubmit tracks\nhttp://mrsuicidesheep.tracksubmit.com/submit/",
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
                    "playlistId": "PLFp2-gAWp2eVjZYkT502Xd0tMHFD0YjP9",
                    "position": 2,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": "JhGkt6PQQ8E"
                    }
                }
            },
            {
                "id": "PL2qvtSnCzogLZMGwm6eJnnKQxRdQlghMPqvc4u77Jth0",
                "snippet": {
                    "publishedAt": "2015-07-14T10:28:10.000Z",
                    "channelId": "UC8iUi9DiP_Nr6uAuo7W74XQ",
                    "title": "Galantis - Louder, Harder, Better",
                    "description": "This is just incredible! Best track from the Galantis album in my opinion.\nDownload... http://bit.ly/1Ca0aWz\n\nGalantis\nhttps://soundcloud.com/wearegalantis\nhttps://www.facebook.com/wearegalantis\nhttps://twitter.com/wearegalantis\nhttps://www.youtube.com/user/galantistv\n\nReleased by Atlantic Records\nhttp://www.atlanticrecords.com/\nhttps://twitter.com/atlanticrecords\nhttps://soundcloud.com/atlanticrecords\nhttps://www.facebook.com/atlanticrecords\nhttps://www.youtube.com/user/atlanticvideos\n\nArtwork from Kisaragi Kancolle\n\nFacebooobs\nhttps://www.facebook.com/MrSuicideSheep\n\nFollow on Soundcloud\nhttps://soundcloud.com/mrsuicidesheep\n\nFollow on Twitter\nhttps://twitter.com/mrsuicidesheep\n\nSheepy t-shirts!\nhttp://bit.ly/Sheepytees\n\nSubmit tracks\nhttp://mrsuicidesheep.tracksubmit.com/submit/",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/hAtB3ZWs--c/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/hAtB3ZWs--c/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/hAtB3ZWs--c/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/hAtB3ZWs--c/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        },
                        "maxres": {
                            "url": "https://i.ytimg.com/vi/hAtB3ZWs--c/maxresdefault.jpg",
                            "width": 1280,
                            "height": 720
                        }
                    },
                    "channelTitle": "SpamWeb",
                    "playlistId": "PLFp2-gAWp2eVjZYkT502Xd0tMHFD0YjP9",
                    "position": 3,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": "hAtB3ZWs--c"
                    }
                }
            }
        ]
    }
    '''
    for item in playlist_items["items"]:
        item["snippet"]["publishedAt"] = datetime.strptime(item["snippet"]["publishedAt"], '%Y-%m-%dT%H:%M:%S.000Z')

    context = {
        'playlist_items': playlist_items,
    }
    return render(request, 'spamusic/playlist-videos.html', context)


# Va chercher les details d'une playlist et le rend via un template
@login_required()
def ajax_details_playlist(request):
    playlist_id = request.POST['playlist_id']
    master = f.get_youtube_master()
    check = f.check_youtube_master(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    check = f.check_api_token(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    else:
        credential = check['value']

    youtube = f.build_youtube(credential)
    playlist_response = f.playlist_details(youtube=youtube, playlist_id=playlist_id)
    '''
    playlist_response = {
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
                },
                "player": {
                    "embedHtml": "<iframe type='text/html' src='http://www.youtube.com/embed/videoseries?list=PLFp2-gAWp2eVjZYkT502Xd0tMHFD0YjP9' width='640' height='360' frameborder='0' allowfullscreen='true'/>"
                }
            }
        ]
    }
    '''
    playlist = playlist_response["items"][0]
    playlist["snippet"]["publishedAt"] = datetime.strptime(playlist["snippet"]["publishedAt"], '%Y-%m-%dT%H:%M:%S.000Z')
    context = {
        'playlist': playlist,
    }
    return render(request, 'spamusic/main-content.html', context)


# lance une recherche youtube avec les mots clé passés en parametres
@login_required()
def ajax_rechercher_videos(request):
    q = request.POST['q']
    master = f.get_youtube_master()
    check = f.check_youtube_master(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    check = f.check_api_token(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    else:
        credential = check['value']

    youtube = f.build_youtube(credential)
    video_list = f.search_video_list(youtube=youtube, q=q)

    '''
    video_list = {
        "nextPageToken": "CAUQAA",
        "items": [
            {
                "id": {
                    "kind": "youtube#video",
                    "videoId": "lki1y2wa820"
                },
                "snippet": {
                    "publishedAt": "2014-08-29T19:00:03.000Z",
                    "channelId": "UC5nc_ZtjKW1htCVZVRxlQAQ",
                    "title": "'Taking You Higher Pt. 3' (Progressive House Mix)",
                    "description": "The new 'Taking You Higher' is finally here! Any support is truly appreciated. Download on iTunes... http://bit.ly/YJBeIg Listen on Spotify... http://spoti.fi/1Cazg2Y ...",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/lki1y2wa820/default.jpg"
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/lki1y2wa820/mqdefault.jpg"
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/lki1y2wa820/hqdefault.jpg"
                        }
                    },
                    "channelTitle": "MrSuicideSheep",
                    "liveBroadcastContent": "none"
                }
            },
            {
                "id": {
                    "kind": "youtube#video",
                    "videoId": "N2mVfpDHr9k"
                },
                "snippet": {
                    "publishedAt": "2012-03-09T15:14:44.000Z",
                    "channelId": "UC5nc_ZtjKW1htCVZVRxlQAQ",
                    "title": "'Peaceful Solitude' Mix",
                    "description": "Yipeee another mix :D As usual the tracks were chosen by myself and this time mixed by Aaron Static. Go give him your love. When I uploaded 'Burning ...",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/N2mVfpDHr9k/default.jpg"
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/N2mVfpDHr9k/mqdefault.jpg"
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/N2mVfpDHr9k/hqdefault.jpg"
                        }
                    },
                    "channelTitle": "MrSuicideSheep",
                    "liveBroadcastContent": "none"
                }
            },
            {
                "id": {
                    "kind": "youtube#video",
                    "videoId": "heJBwBUStXU"
                },
                "snippet": {
                    "publishedAt": "2013-07-19T16:30:15.000Z",
                    "channelId": "UC5nc_ZtjKW1htCVZVRxlQAQ",
                    "title": "'Taking You Higher Pt. 2' (Progressive House Mix)",
                    "description": "'Taking You Higher' Pt. 3 Support here... http://bit.ly/YJBeIg So a year after 'Taking You Higher' Rameses B and I decided to put out another summery ...",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/heJBwBUStXU/default.jpg"
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/heJBwBUStXU/mqdefault.jpg"
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/heJBwBUStXU/hqdefault.jpg"
                        }
                    },
                    "channelTitle": "MrSuicideSheep",
                    "liveBroadcastContent": "none"
                }
            },
            {
                "id": {
                    "kind": "youtube#video",
                    "videoId": "waYpEQAYf3g"
                },
                "snippet": {
                    "publishedAt": "2015-06-19T17:28:39.000Z",
                    "channelId": "UC5nc_ZtjKW1htCVZVRxlQAQ",
                    "title": "Taking You Deeper (Deep House Mix)",
                    "description": "First deep house mix! \"This mix represents the greatest adventure in life. We all begin in the same place: open, excited, and slightly uncertain. The road is filled ...",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/waYpEQAYf3g/default.jpg"
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/waYpEQAYf3g/mqdefault.jpg"
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/waYpEQAYf3g/hqdefault.jpg"
                        }
                    },
                    "channelTitle": "MrSuicideSheep",
                    "liveBroadcastContent": "none"
                }
            },
            {
                "id": {
                    "kind": "youtube#video",
                    "videoId": "2td5Nj23vns"
                },
                "snippet": {
                    "publishedAt": "2015-01-01T19:01:08.000Z",
                    "channelId": "UC5nc_ZtjKW1htCVZVRxlQAQ",
                    "title": "'Dawn' Pt. 2 (An Ambient Mix)",
                    "description": "Hey everyone, after exactly 2 years I've finally managed to bring you the next instalment of the ambient mix. I really hope you guys enjoy it! This mix is supposed ...",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/2td5Nj23vns/default.jpg"
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/2td5Nj23vns/mqdefault.jpg"
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/2td5Nj23vns/hqdefault.jpg"
                        }
                    },
                    "channelTitle": "MrSuicideSheep",
                    "liveBroadcastContent": "none"
                }
            }
        ]
    }
    '''
    for video in video_list["items"]:
        video["snippet"]["publishedAt"] = datetime.strptime(video["snippet"]["publishedAt"], '%Y-%m-%dT%H:%M:%S.000Z')

    context = {
        'video_list': video_list,
        'q': q,
    }
    return render(request, 'spamusic/yt-tab-search-results.html', context)


def ajax_add_video_to_playlist(request):
    playlist_id = request.POST['playlist_id']
    video_id = request.POST['video_id']
    master = f.get_youtube_master()
    check = f.check_youtube_master(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    check = f.check_api_token(request=request, master=master)
    if check['status'] is False:
        return HttpResponseForbidden()
    else:
        credential = check['value']

    youtube = f.build_youtube(credential)
    playlist_item = f.add_video_to_playlist(youtube=youtube, playlist_id=playlist_id, video_id=video_id)

    '''
    playlist_item = {
        "kind": "youtube#playlistItem",
        "etag": "\"iDqJ1j7zKs4x3o3ZsFlBOwgWAHU/vryJ8ygeWBRZUjiy8BfF18P1YtA\"",
        "id": "PL2qvtSnCzogLZMGwm6eJnnGEPUzm2ky4yVXxf1rDXRqY",
        "snippet": {
            "publishedAt": "2015-07-15T18:42:20.000Z",
            "channelId": "UC8iUi9DiP_Nr6uAuo7W74XQ",
            "title": "Uppermost - Disco Kids",
            "description": "Uppermost is back with some Disco! :P\nDownload... http://apple.co/1F8CbgP\n\nUppermost\nhttps://soundcloud.com/uppermost\nhttps://www.youtube.com/user/uppermostmusic\nhttps://twitter.com/uppermostmusic\nhttps://www.facebook.com/uppermost\nhttp://www.uppermostmusic.com/\n\nFacebooobs\nhttps://www.facebook.com/MrSuicideSheep\n\nFollow on Soundcloud\nhttps://soundcloud.com/mrsuicidesheep\n\nFollow on Twitter\nhttps://twitter.com/mrsuicidesheep\n\nSheepy t-shirts!\nhttp://bit.ly/Sheepytees\n\nSubmit tracks\nhttp://mrsuicidesheep.tracksubmit.com/submit/",
            "thumbnails": {
                "default": {
                    "url": "https://i.ytimg.com/vi/_i2EnWgpwjc/default.jpg",
                    "width": 120,
                    "height": 90
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/_i2EnWgpwjc/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "high": {
                    "url": "https://i.ytimg.com/vi/_i2EnWgpwjc/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "standard": {
                    "url": "https://i.ytimg.com/vi/_i2EnWgpwjc/sddefault.jpg",
                    "width": 640,
                    "height": 480
                },
                "maxres": {
                    "url": "https://i.ytimg.com/vi/_i2EnWgpwjc/maxresdefault.jpg",
                    "width": 1280,
                    "height": 720
                }
            },
            "channelTitle": "SpamWeb",
            "playlistId": "PLFp2-gAWp2eVjZYkT502Xd0tMHFD0YjP9",
            "resourceId": {
                "kind": "youtube#video",
                "videoId": "_i2EnWgpwjc"
            }
        }
    }
    '''
    playlist_item["snippet"]["publishedAt"] = datetime.strptime(playlist_item["snippet"]["publishedAt"],
                                                                '%Y-%m-%dT%H:%M:%S.000Z')
    add_log(text="%s a ajouté une nouvelle vidéo : %s" % (request.user.username, playlist_item["snippet"]["title"]),
            app="spamusic",
            log_type="spamusic_add_video",
            user=request.user)

    context = {
        'playlist_item': playlist_item,
    }
    return render(request, 'spamusic/new-video.html', context)
