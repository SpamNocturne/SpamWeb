from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: ajax/jiec/
    # POST : 'idee_id' et 'com'
    url(r'^jiec/', views.jacquesIdeaEnregistrerCommentaire, name='jacquesIdeaEnregistrerCommentaire'),
    url(r'^jidv/', views.jacquesIdeaDownvote, name='jacquesIdeaDownvote'),
    url(r'^jiuv/', views.jacquesIdeaUpvote, name='jacquesIdeaUpvote'),
]