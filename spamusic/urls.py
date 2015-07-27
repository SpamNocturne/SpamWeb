# -*- coding: utf-8 -*-
from django.conf.urls import url

<<<<<<< HEAD
from . import views
=======
from . import views, ajax
>>>>>>> 0a362510ac2175dad2071591e7baf7debc9d6dbe

urlpatterns = [
    # ex: /spamusic/OAuthAuthentification
    # url(r'^OAuthAuthentification', views.OAuthAuthentification, name='OAuthAuthentification'),
    # ex: /spamusic/OAuthReturn
    url(r'^OAuthReturn', views.OAuthReturn, name='OAuthReturn'),
<<<<<<< HEAD
=======

    url(r'^ajax/sm_ap/', ajax.ajax_ajouter_playlist, name='ajax_ajouter_playlist'),
    url(r'^ajax/sm_dp/', ajax.ajax_details_playlist, name='ajax_details_playlist'),
    url(r'^ajax/sm_pi/', ajax.ajax_playlistitems, name='ajax_playlistitems'),
    url(r'^ajax/sm_rv/', ajax.ajax_rechercher_videos, name='ajax_rechercher_videos'),
    url(r'^ajax/sm_avtp/', ajax.ajax_add_video_to_playlist, name='ajax_add_video_to_playlist'),


>>>>>>> 0a362510ac2175dad2071591e7baf7debc9d6dbe
    # ex: /spamusic/
    url(r'^', views.index, name='index'),
]