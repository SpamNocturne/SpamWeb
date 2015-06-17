from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from jacquesIdea.models import Idee, Commentaire


def jacquesIdeaEnregistrerCommentaire(request):
    #recuperation des parametre
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

    #generation du template
    context = {'commentaire': com}
    return render(request, 'ajax/rightComment.html', context)