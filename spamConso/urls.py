# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^GBienBuGBienMangé', views.index, name='index'),
    url(r'^add_conso', views.add_conso, name = 'add_conso'),
    url(r'^consos', views.conso_view, name = 'conso_view'),

]