# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class UtilisateurStats(models.Model):
    nom_fb = models.CharField(max_length=250, unique=True)

    def get_mots_plus_utilises(self, nb = 0):
        all_mots_tris = MotScore.objects.filter(user = self).order_by("-score")
        if nb != 0:
            all_mots_tris = all_mots_tris[:nb]
        return all_mots_tris

    def __str__(self):
        return "{0}".format(self.nom_fb)


class MotScore(models.Model):
    user = models.ForeignKey(UtilisateurStats)

    mot = models.CharField(max_length=500)
    score = models.IntegerField(default=0, null=False)
    class Meta:
        unique_together = ("user", "mot")

    def __str__(self):
        return "{0} ({1}) ({2})".format(self.mot, self.score, self.user)

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

    def __str__(self):
        return "{0} (le {1})".format(self.texte, self.date)

