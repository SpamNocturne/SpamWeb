# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^get_conso', views.get_conso, name='get_conso'),
    url(r'^add_conso', views.add_conso, name = 'add_conso'),

]