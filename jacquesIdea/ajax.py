from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from home.log import add_log
from jacquesIdea.models import Idee, Commentaire


@login_required
def ajax_enregistrer_commentaire(request):
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

    add_log(text="%s a commenté l'idée : %s" % (request.user.username, com.idee.titre),
            app="jacquesIdea",
            log_type="jacquesIdea_comment",
            user=request.user)

    # generation du template
    context = {'commentaire': com}
    return render(request, 'jacquesIdea/rightComment.html', context)


@login_required
def ajax_downvote(request):
    # recupération des parametres
    idee_id = request.POST['idee_id']
    # user_id = request.POST['idee_id']
    idee = get_object_or_404(Idee, pk=idee_id)
    # DownVote
    vote = idee.get_vote_from(request.user)
    vote.downvote()
    vote.save()
    add_log(text="%s n'aime pas l'idée : %s" % (request.user.username, idee.titre),
            app="jacquesIdea",
            log_type="jacquesIdea_vote",
            user=request.user)
    return HttpResponse()


@login_required
def ajax_upvote(request):
    # recupération des parametres
    idee_id = request.POST['idee_id']
    # user_id = request.POST['idee_id']
    idee = get_object_or_404(Idee, pk=idee_id)
    # DownVote
    vote = idee.get_vote_from(request.user)
    vote.upvote()
    vote.save()
    add_log(text="%s aime l'idée : %s" % (request.user.username, idee.titre),
            app="jacquesIdea",
            log_type="jacquesIdea_vote",
            user=request.user)
    return HttpResponse()


@login_required
def ajax_supprimer_idee(request):
    # recupération des parametres
    idee_id = request.POST['idee_id']
    if idee_id is None:
        return HttpResponseBadRequest()
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
    add_log(text="%s a supprimé l'idée : %s" % (request.user.username, idee.titre),
            app="jacquesIdea",
            log_type="jacquesIdea_delete_idea",
            user=request.user)
    return HttpResponse()


@login_required
def ajax_valider_idee(request):
    # recupération des parametres
    idee_id = request.POST['idee_id']
    if idee_id is None:
        return HttpResponseBadRequest()
    idee = get_object_or_404(Idee, pk=idee_id)
    # on vérifie que l'idée appartient bien a l'utilisateur connecté
    if idee.auteur != request.user:
        return HttpResponseForbidden()
    # validation
    idee.statut = idee.STATUTS["VALIDATED"]
    idee.save()
    add_log(text="%s a validé l'idée : %s" % (request.user.username, idee.titre),
            app="jacquesIdea",
            log_type="jacquesIdea_validate_idea",
            user=request.user)
    return HttpResponse()


