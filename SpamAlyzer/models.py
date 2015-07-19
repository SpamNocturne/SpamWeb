# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

class UtilisateurStats(models.Model):
    nom_fb = models.CharField(max_length=250)
    nb_de_messages = models.IntegerField(default=0)

class FichierSoumis(models.Model):
    auteur = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    fichier = models.FileField(upload_to='uploads/SpamAlyzer/%Y-%m-%d/')

class Message(models.Model):
    texte = models.CharField(max_length=5000)
    auteur = models.ForeignKey(UtilisateurStats)
    date = models.DateField()
    file = models.ForeignKey(FichierSoumis)


