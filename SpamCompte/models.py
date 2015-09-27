# coding: utf8
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
import operator


def equilibrer(a_equilibrer, equilibrage):
    # le dernier paye tout ce qu'il peut au 1er
    a_payer = min(abs(a_equilibrer[0][1]), abs(a_equilibrer[-1][1]))
    a_equilibrer[0] = (a_equilibrer[0][0], a_payer + a_equilibrer[0][1])
    a_equilibrer[-1] = (a_equilibrer[-1][0], a_equilibrer[-1][1] - a_payer)
    # on enregistre ce paiement
    equilibrage.append((a_equilibrer[0][0], a_equilibrer[-1][0], a_payer))
    # on supprime les montants nuls
    a_supprimer = []
    for t in a_equilibrer:
        if t[1] == Decimal(0.00):
            a_supprimer.append(t)
    for t in a_supprimer:
        a_equilibrer.remove(t)
    if len(a_equilibrer) == 0:
        return equilibrage
    # on continue avec la meme liste (retriée)
    a_equilibrer.sort(key=lambda tup: tup[1])
    return equilibrer(a_equilibrer, equilibrage)


class BattleDArgent(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    participants = models.ManyToManyField(User, blank=True)
    pub_date = models.DateTimeField(blank=True, null=True)

    def balance(self):
        return {}

    def __str__(self):
        return self.nom

    def calcul_score(self):
        score_participants = {}
        for p in self.participants.all():
            score_participants[p.username] = 0
        for conso in self.depense_set.all():
            for s_c in conso.spammeurconsommateur_set.all():
                score_participants[s_c.user.username] += s_c.montant_depense - s_c.montant_utilise
        return score_participants

    def calcul_equilibre(self):
        equilibrage = []
        score_participants = self.calcul_score()
        equilibrage = equilibrer(sorted(score_participants.items(), key=operator.itemgetter(1)), equilibrage)
        return score_participants, equilibrage


class Depense(models.Model):
    # une description rapide
    description = models.TextField()
    # la battle associée (le conteneur de toutes les dépenses permmettant de faire la somme finale)
    my_son_my_battle = models.ForeignKey(BattleDArgent)
    # date de creation ou de mise à jour
    date = models.DateTimeField(blank=True, null=True)

    def argent_depense(self):
        total = Decimal(0.00)
        for s_c in self.spammeurconsommateur_set.all():
            total += abs(s_c.montant_depense)
        return total


class SpammeurConsommateur(models.Model):
    # lié à un vrai membre du Spam
    user = models.ForeignKey(User, related_name='mes_transactions')
    # montant dépense (en euros pour l'instant).
    # ex: l'user a payé 50€
    montant_depense = models.DecimalField(default=0, decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.00'))])
    # montant utilisé
    # ex: l'user n'a utilisé que 15€ de ces 50€, le reste est pour d'autres users
    montant_utilise = models.DecimalField(default=0, decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.00'))])
    # la depense associee
    depense_pour_laquelle_on_contribue = models.ForeignKey(Depense, null=True, blank=True)
