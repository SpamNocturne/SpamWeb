from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: jiec/
    # POST : 'idee_id' et 'com'
    url(r'^jiec/', views.jacquesIdeaEnregistrerCommentaire, name='jacquesIdeaEnregistrerCommentaire'),
]