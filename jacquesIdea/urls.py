from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /XXX/
    url(r'^', views.index, name='index'),
]