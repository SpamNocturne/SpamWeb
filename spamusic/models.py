from django.contrib.auth.models import User
from django.db import models

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField

# Cette classe permet de stocker les credentials et aurorisation pour l'OAuth2
# Nottement pour la communication avec la Youtube API V3
# Comme l'objectif de spamusic est d'avoir une playlist collaborative,
#   cette table ne servira que pour un seul utilisateur
# Cet user doit exister en base, être admin et se nommer 'spamadmin' avec le mot de passe 'spamnocturne'
#  TODO FIXTURES POUR CREER L'ADMIN PROPRIETAIRE DE LA PLAYLIST


class CredentialsYoutubeModel(models.Model):
    id = models.OneToOneField(User, primary_key=True)
    credential = CredentialsField()
