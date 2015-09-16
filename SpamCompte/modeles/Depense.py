# coding: utf8
from . import SpameurConsommateur, BattleDArgent

class Depense(models.Model):
    # ceux qui ont payé
    payeurs = models.ManyToManyField(SpameurConsommateur)
    # pour qui ils ont payé
    beneficiaires = models.ManyToManyField(SpameurConsommateur)
    # la battle associée (le conteneur de toutes les dépenses permmettant de faire la somme finale)
    my_son_my_battle = models.ForeignKey(BattleDArgent)