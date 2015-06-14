from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /user/login
    url(r'^login$', views.connexion, name='connexion'),
    # ex: /user/login
    url(r'^register', views.inscription, name='inscription'),
    # ex: /user/logout
    url(r'^logout$', views.deconnexion, name='deconnexion'),
    # ex: /user/password_change_done
    url(r'^password_change_done$', views.password_change_done, name='password_change_done'),
    # ex: /user/password_change
    url(r'^password_change$', views.password_change, name='password_change'),
]