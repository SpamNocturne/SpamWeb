from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: ajax/jiec/
    # POST : 'idee_id' et 'com'
    url(r'^ji_ec/', views.jacquesIdeaEnregistrerCommentaire, name='jacquesIdeaEnregistrerCommentaire'),
    url(r'^ji_dv/', views.jacquesIdeaDownvote, name='jacquesIdeaDownvote'),
    url(r'^ji_uv/', views.jacquesIdeaUpvote, name='jacquesIdeaUpvote'),
    url(r'^ji_si/', views.jacquesIdeaSupprimerIdee, name='jacquesIdeaSupprimerIdee'),

    url(r'^sm_ap/', views.spamusicAjouterPlaylist, name='spamusicAjouterPlaylist'),
    url(r'^sm_dp/', views.spamusicDetailsPlaylist, name='spamusicDetailsPlaylist'),
]