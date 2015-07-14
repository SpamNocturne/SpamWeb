from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.datetime_safe import datetime
from jacquesIdea.models import Idee, Commentaire
from spamusic import functions as f

'''
    AJAX JACQUESIDEA
'''
ONLINE = False


@login_required
def jacquesIdeaEnregistrerCommentaire(request):
    # recuperation des parametres
    idee_id = request.POST['idee_id']
    commentaire_text = request.POST['com']
    idee = get_object_or_404(Idee, pk=idee_id)

    # Creation du commentaire
    com = Commentaire()
    com.idee = idee
    com.auteur = request.user
    com.commentaire_text = commentaire_text
    com.pub_date = timezone.now()
    com.save()

    # generation du template
    context = {'commentaire': com}
    return render(request, 'ajax/rightComment.html', context)


@login_required
def jacquesIdeaDownvote(request):
    # recupération des parametres
    idee_id = request.POST['idee_id']
    # user_id = request.POST['idee_id']
    idee = get_object_or_404(Idee, pk=idee_id)
    # DownVote
    vote = idee.get_vote_from(request.user)
    vote.downvote()
    vote.save()
    return HttpResponse()


@login_required
def jacquesIdeaUpvote(request):
    # recupération des parametres
    idee_id = request.POST['idee_id']
    # user_id = request.POST['idee_id']
    idee = get_object_or_404(Idee, pk=idee_id)
    # DownVote
    vote = idee.get_vote_from(request.user)
    vote.upvote()
    vote.save()
    return HttpResponse()


@login_required
def jacquesIdeaSupprimerIdee(request):
    # recupération des parametres
    idee_id = request.POST['idee_id']
    idee = get_object_or_404(Idee, pk=idee_id)
    # on vérifie que l'idée appartient bien a l'utilisateur connecté
    if idee.auteur != request.user:
        return HttpResponseForbidden()
    # On supprime les commentaires (automatique en fait :D)
    # idee.commentaire_set.all().delete()
    # On supprime les votes (automatique en fait :D)
    # idee.votants.clear()
    # On supprime l'idée
    idee.delete()
    return HttpResponse()


'''
    AJAX SPAMUSIC
'''


# Va chercher toutes les playlistes du master et les rend en template
@login_required()
def spamusicAjouterPlaylist(request):
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
    context = {'playlist': playlist}
    return render(request, 'spamusic/control-sidebar-playlist.html', context)


# récupère les élément d'une playlist et les rend l'onglet video les contenants
@login_required()
def spamusicPlaylistItems(request):
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
        'cpt': len(playlist_items["items"])
    }
    return render(request, 'spamusic/playlist-videos.html', context)


# Va chercher les details d'une playlist et le rend via un template
@login_required()
def spamusicDetailsPlaylist(request):
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
    context = {'playlist': playlist}
    return render(request, 'spamusic/main-content.html', context)
