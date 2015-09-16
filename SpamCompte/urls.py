# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /spamCompte/
    url(r'^', views.index, name='index'),
]