# -*- coding: utf-8 -*-
from django import forms
from .models import BattleDArgent
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxSelectMultiple


class BattleDArgentForm(forms.ModelForm):
    class Meta:
        model = BattleDArgent
        fields = ["nom", "participants"]
        labels = {
            'nom': "Nom du SpamCompte",
            'participants': "Ajouter des participants",
        }

    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users', [])
        super(BattleDArgentForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs \
            .update({
                'placeholder': "ex: Holidays!",
                'class': 'form-control'
            })
        self.fields['participants'].widget.attrs \
            .update({
                'class': 'form-control'
            })
        self.fields['participants'].widget = CheckboxSelectMultiple()
        self.fields['participants'].queryset = User.objects.exclude(pk__in=self.users)

    def clean_participants(self):
        # on ajoute les users déjà présents sur le SpamCompte (ou le user créateur du SpamCompte)
        participants_choisis = self.cleaned_data['participants'].all()
        wanted_participants = []
        for participant in participants_choisis:
            wanted_participants.append(participant.pk)
        wanted_participants.extend(self.users)
        participants_plus_user = User.objects.filter(pk__in=wanted_participants)
        return participants_plus_user
