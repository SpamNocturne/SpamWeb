from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from jacquesIdea.models import Idee, Commentaire

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