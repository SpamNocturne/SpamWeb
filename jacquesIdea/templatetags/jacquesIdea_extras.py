from django import template
from jacquesIdea.models import Idee

register = template.Library()


@register.filter()
# prend une idée et un user retourne vrai si le user a upvoted, false sinon
def is_upvoted_by(idea, user):
    return idea.is_upvoted_by(user)


@register.filter()
def is_downvoted_by(idea, user):
    return idea.is_downvoted_by(user)


@register.filter()
def is_pending(idea):
    return idea.statut == Idee.STATUTS["PENDING"]


@register.filter()
def is_validated(idea):
    return idea.statut == Idee.STATUTS["VALIDATED"]


@register.simple_tag()
def get_idea_statut(key):
    return Idee.STATUTS.get(key)
