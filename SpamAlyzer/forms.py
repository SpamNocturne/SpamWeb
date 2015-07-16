__author__ = 'David'

from django.forms import ModelForm
from .models import FichierSoumis

class FichierSoumisForm(ModelForm):
    class Meta:
        model = FichierSoumis
        fields = ('fichier', )
        labels = {'fichier' : 'Archive des messages Facebook : ', }