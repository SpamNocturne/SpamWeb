from django import template
from jacquesIdea.models import Idee

register = template.Library()

#prend une idée et un user retourne vrai si le user a upvoted, false sinon
@register.filter()
def is_upvoted_by(idea, user):
    return idea.is_upvoted_by(user)\

@register.filter()
def is_downvoted_by(idea, user):
    return idea.is_downvoted_by(user)