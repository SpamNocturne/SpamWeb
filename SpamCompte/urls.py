# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: spamCompte/ajout/
    url(r'^ajout/$', views.ajout_battle, name='ajout_battle'),
    # ex: spamCompte/ajout/
    url(r'^consulterBattle/([0-9]+)/$', views.consulter_battle, name='consulter_battle'),
    # ex: spamCompte/
    url(r'^$', views.index, name='index'),
]