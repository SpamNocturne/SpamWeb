# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
from . import ajax

urlpatterns = [
    # ex: /jacques/idea/a/dit/new/idea/
    url(r'^new/idea/', views.createIdea, name='createIdea'),

    # ajax
    url(r'^ajax/ji_ec/', ajax.ajax_enregistrer_commentaire, name='ajax_enregistrer_commentaire'),
    url(r'^ajax/ji_dv/', ajax.ajax_downvote, name='ajax_downvote'),
    url(r'^ajax/ji_uv/', ajax.ajax_upvote, name='ajax_upvote'),
    url(r'^ajax/ji_si/', ajax.ajax_supprimer_idee, name='ajax_supprimer_idee'),


    # ex: /jacques/idea/a/dit/
    url(r'^', views.index, name='index'),
]