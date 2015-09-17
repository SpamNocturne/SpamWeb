# coding: utf8
from django.db import models
from django.contrib.auth.models import User


class SpammeurConsommateur(models.Model):
    # lié à un vrai membre du Spam
    user = models.ForeignKey(User, related_name='mes_transactions')
    # montant dépense (en euros pour l'instant)
    montant_depense = models.PositiveIntegerField()


class BattleDArgent(models.Model):
    nom = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, blank=True)
    pub_date = models.DateTimeField(blank=True, null=True)

    def balance(self):
        return {}

    def __str__(self):
        return self.nom


class Depense(models.Model):
    # une description rapide
    description = models.TextField()
    # ceux qui ont payé
    payeurs = models.ManyToManyField(SpammeurConsommateur, related_name='mes_depenses_pour_des_spammeurs')
    # pour qui ils ont payé
    beneficiaires = models.ManyToManyField(SpammeurConsommateur, related_name='mes_achats_que_je_dois_rembourser')
    # la battle associée (le conteneur de toutes les dépenses permmettant de faire la somme finale)
    my_son_my_battle = models.ForeignKey(BattleDArgent)
    date = models.DateTimeField(blank=True, null=True)

