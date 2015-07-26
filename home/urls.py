from django.conf.urls import url

from . import views, ajax

urlpatterns = [
    # ajax
    url(r'^ajax/ho_gn/', ajax.ajax_get_notifications, name='ajax_get_notifications'),
    # ajax
    url(r'^ajax/ho_dl/', ajax.ajax_delete_unseen_log, name='ajax_delete_unseen_log'),

    # ex: /user/login
    url(r'^$', views.index, name='index'),
]