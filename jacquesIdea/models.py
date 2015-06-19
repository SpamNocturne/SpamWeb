import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Idee(models.Model):
    titre = models.CharField(max_length=150)
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

    def is_upvoted_by(self, user):
        vote = Vote.objects.filter(auteur=user, idee=self)
        if vote:
            #Si il y a un vote, il ne peut y en avoir qu'un ! contrainte UNIQUE
            if vote[0].valeur > 0:
                return True
        return False

    def is_downvoted_by(self, user):
        vote = Vote.objects.filter(auteur=user, idee=self)
        if vote:
            #Si il y a un vote, il ne peut y en avoir qu'un ! contrainte UNIQUE
            if vote[0].valeur < 0:
                return True
        return False

    #Renvoie le vote de l'utilisateur pour cette idee (le cree si inexistant)
    def get_vote_from(self, user):
        vote = Vote.objects.filter(auteur=user, idee=self)
        #s'il y a un vote on le retourne
        if vote:
            return vote[0]
        #s'il n'y a pas de vote on le crée
        else:
            vote = Vote.objects.create(auteur=user, idee=self)
            return vote

    #retourne le calcul des upvote/downvote sur une idée
    @property
    def get_note(self):
        somme = 0
        for vote in self.vote_set.all():
            somme += vote.valeur
        return somme

    @property
    def get_upvotes(self):
        upvotes = []
        for vote in self.vote_set.all():
            if vote.valeur > 0:
                upvotes.append(vote)
        return upvotes

    @property
    def get_downvotes(self):
        downvote = []
        for vote in self.vote_set.all():
            if vote.valeur < 0:
                downvote.append(vote)
        return downvote


class Commentaire(models.Model):
    idee = models.ForeignKey(Idee)
    commentaire_text = models.TextField()
    auteur = models.ForeignKey(User)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.commentaire_text


#un vote est lie a un user et une idee
class Vote(models.Model):
    # ici meta sert a avoir une clé primaire sur deux champs
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