import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Idee(models.Model):
    titre = models.CharField(max_length=50)
    idee_text = models.TextField()
    pub_date = models.DateTimeField()
    auteur = models.ForeignKey(User, related_name='idees')
    votants = models.ManyToManyField(User, through='Vote')

    def __str__(self):
        return self.titre

    #determine si une idee est recente (moins d'une semaine)
    def est_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now
    est_recent.admin_order_field = 'pub_date'
    est_recent.boolean = True
    est_recent.short_description = 'recent ?'


class Commentaire(models.Model):
    idee = models.ForeignKey(Idee)
    commentaire_text = models.TextField()
    auteur = models.ForeignKey(User)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.commentaire_text


#un vote est lie a un user et une idee
class Vote(models.Model):
    class Meta:
          unique_together = ('auteur', 'idee')
    auteur = models.ForeignKey(User)
    idee = models.ForeignKey(Idee)
    valeur = models.IntegerField(default=0)

    def __str__(self):
        return self.auteur.username + " voted for " + str(self.idee) + " : " + str(self.valeur)

    def upvote(self):
        self.valeur = 1

    def downvote(self):
        self.valeur = -1