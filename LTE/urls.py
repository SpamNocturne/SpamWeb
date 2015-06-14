from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /LTE/
    url(r'^$', views.index, name='index'),
]