# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views, ajax

urlpatterns = [
    # ex: /spamusic/OAuthAuthentification
    # url(r'^OAuthAuthentification', views.OAuthAuthentification, name='OAuthAuthentification'),
    # ex: /spamusic/OAuthReturn
    url(r'^OAuthReturn', views.OAuthReturn, name='OAuthReturn'),

    url(r'^ajax/sm_ap/', ajax.ajax_ajouter_playlist, name='ajax_ajouter_playlist'),
    url(r'^ajax/sm_dp/', ajax.ajax_details_playlist, name='ajax_details_playlist'),
    url(r'^ajax/sm_pi/', ajax.ajax_playlistitems, name='ajax_playlistitems'),
    url(r'^ajax/sm_rv/', ajax.ajax_rechercher_videos, name='ajax_rechercher_videos'),
    url(r'^ajax/sm_avtp/', ajax.ajax_add_video_to_playlist, name='ajax_add_video_to_playlist'),


    # ex: /spamusic/
    url(r'^', views.index, name='index'),
]