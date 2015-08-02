__author__ = 'david'

from django import forms

from SpamAlyzer.models import FichierSoumis


class FichierSoumisForm(forms.ModelForm):
    class Meta:
        model = FichierSoumis
        fields = ["fichier"]