# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^conversation/spam/web/(?P<num_page>[0-9]+)', views.conversation, name="conversation"),
    url(r'^historique/depot', views.historique, name="histoDepot"),
    url(r'^stats/globales', views.statsGlobales, name="statsGlobales"),
    url(r'^stats/spammeurs', views.statsSpammeurs, name="statsSpammeurs"),
    url(r'^stats/mec/ou/fille/de/nom/(?P<id_pers>[0-9]+)', views.statsMec, name="statsMec"),
]