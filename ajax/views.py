from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from jacquesIdea.models import Idee, Commentaire
from spamusic import functions as f


'''
    AJAX JACQUESIDEA
'''
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
    playlist = f.playlist_details(youtube=youtube, playlist_id=playlist_id)
    context = {'playlist': playlist["items"][0]}
    return render(request, 'spamusic/main-content.html', context)
