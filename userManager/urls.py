from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /user/login
    url(r'^login$', views.connexion, name='connexion'),
    # ex: /user/logout
    url(r'^logout$', views.deconnexion, name='deconnexion'),

    #url(r'^connexion$', 'django.contrib.auth.views.login', {'template_name': 'userManager/connexion.html'}),
    url(r'^password_change_done$', views.password_change_done, name='password_change_done'),
    url(r'^password_change$', views.password_change, name='password_change'),
]