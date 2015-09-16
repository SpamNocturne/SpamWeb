# coding: utf8
from django.contrib.auth.models import User


class SpameurConsommateur(models.Model):
    # lié à un vrai membre du Spam
    user = models.ForeignKey(User, related_name='mes_transactions')
    # dépense OU crédite (donc peut être négatif)
    montant_depense = models.IntegerField()