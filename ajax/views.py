from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from jacquesIdea.models import Idee, Commentaire


def jacquesIdeaEnregistrerCommentaire(request):
    idee_id = request.POST['idee_id']
    commentaire_text = request.POST['com']
    idee = get_object_or_404(Idee, pk=idee_id)
    com = Commentaire()
    com.idee = idee
    com.auteur = request.user
    com.commentaire_text = commentaire_text
    com.pub_date = timezone.now()
    com.save()
    return HttpResponse()