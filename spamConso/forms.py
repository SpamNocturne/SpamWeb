from django import forms
from .models import Consommation

class ConsoForm(forms.ModelForm):
    class Meta:
        model = Consommation
        fields = ["type", "description"]
        labels = {
            'type': "Type",
            'description': "Description",
        }

    def __init__(self, *args, **kwargs):
        super(ConsoForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.attrs\
            .update({
                'placeholder': "Type de conso",
                'class': 'form-control'
            })
        self.fields['description'].widget.attrs\
            .update({
                'placeholder': "C'était bon ?",
                'class': 'form-control'
            })