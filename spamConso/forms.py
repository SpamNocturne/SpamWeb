from django import forms
from .models import Consommation

class ConsoForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Consommation
        fields = ["type", "tags", "description"]
        labels = {
            'type': "Type",
            'tags': "Tags",
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