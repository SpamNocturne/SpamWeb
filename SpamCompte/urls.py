# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: spamCompte/ajoutCompte/
    url(r'^ajoutCompte/$', views.ajout_battle, name='ajout_battle'),
    # ex: spamCompte/consulterBattle/5/ajoutDepense/
    url(r'^supprimerCompte/(?P<battle_id>\d+)/$', views.supprimer_compte, name='supprimer_compte'),
    # ex: spamCompte/consulterBattle/5/ajoutDepense/
    url(r'^consulterCompte/(?P<battle_id>\d+)/ajoutDepense/$', views.ajouter_depense, name='ajout_depense'),
    # ex: spamCompte/consulterBattle/5/consulterDepense/1/
    url(r'^consulterCompte/(?P<battle_id>\d+)/consulterDepense/(?P<depense_id>\d+)/$', views.consulter_depense, name='consulter_depense'),
    # ex: spamCompte/consulterBattle/5/supprimerDepense/1/
    url(r'^consulterCompte/(?P<battle_id>\d+)/supprimerDepense/(?P<depense_id>\d+)/$', views.supprimer_depense, name='supprimer_depense'),
    # ex: spamCompte/consulterBattle/5/
    url(r'^consulterCompte/(?P<battle_id>\d+)/$', views.consulter_battle, name='consulter_battle'),
    # ex: spamCompte/
    url(r'^$', views.index, name='index'),
]
