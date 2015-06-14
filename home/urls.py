from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /user/login
    url(r'^$', views.index, name='index'),
]