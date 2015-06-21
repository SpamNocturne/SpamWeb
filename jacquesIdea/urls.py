# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /jacques/idea/a/dit/new/idea/
    url(r'^new/idea/', views.createIdea, name='createIdea'),
    # ex: /jacques/idea/a/dit/
    url(r'^', views.index, name='index'),
]