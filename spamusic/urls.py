# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /spamusic/OAuthAuthentification
    # url(r'^OAuthAuthentification', views.OAuthAuthentification, name='OAuthAuthentification'),
    # ex: /spamusic/OAuthReturn
    url(r'^OAuthReturn', views.OAuthReturn, name='OAuthReturn'),
    # ex: /spamusic/
    url(r'^', views.index, name='index'),
]