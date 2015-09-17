# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: spamCompte/ajoutCompte/
    url(r'^ajoutCompte/$', views.ajout_battle, name='ajout_battle'),
    # ex: spamCompte/consulterBattle/5/ajoutDepense/
    url(r'^consulterBattle/([0-9]+)/ajoutDepense/$', views.ajout_depense, name='ajout_depense'),
    # ex: spamCompte/consulterBattle/5/
    url(r'^consulterBattle/([0-9]+)/$', views.consulter_battle, name='consulter_battle'),
    # ex: spamCompte/
    url(r'^$', views.index, name='index'),
]