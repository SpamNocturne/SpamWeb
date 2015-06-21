from django import forms
from .models import Idee

class IdeeForm(forms.ModelForm):
    class Meta:
        model = Idee
        fields = ["titre", "idee_text"]
        labels = {
            'titre': "Titre",
            'idee_text': "Idée",
        }

    def __init__(self, *args, **kwargs):
        super(IdeeForm, self).__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs\
            .update({
                'placeholder': "Bref résumé",
                'class': 'form-control'
            })
        self.fields['idee_text'].widget.attrs\
            .update({
                'placeholder': "Explication de l'idée",
                'class': 'form-control'
            })