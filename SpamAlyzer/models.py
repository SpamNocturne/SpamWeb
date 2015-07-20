# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

class UtilisateurStats(models.Model):
    nom_fb = models.CharField(max_length=250, unique=True)
    nb_de_messages = models.IntegerField(default=0)

class FichierSoumis(models.Model):
    auteur = models.ForeignKey(User)
    date_depot = models.DateField(auto_now_add=True)
    date_fichier = models.DateField(null=False, auto_now_add=False)
    fichier = models.FileField(upload_to='uploads/SpamAlyzer/%Y-%m-%d/')

class Message(models.Model):
    texte = models.CharField(max_length=5000, null=True)
    auteur = models.ForeignKey(UtilisateurStats)
    date = models.DateTimeField()
    file = models.ForeignKey(FichierSoumis)


