# -*- coding: utf-8 -*-
from django import forms
from decimal import Decimal
from .models import BattleDArgent, Depense, SpammeurConsommateur
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import formset_factory
from django.utils import timezone
from functools import partial, wraps


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


class DepenseForm(forms.Form):
    error_messages = {
        'total_non_nul': "Le total de la transaction n'est pas nul, il y a une différence de : %s€",
        'montant_inutile': "La transaction que vous essayez d'effectuer est inutile. Veuillez remplir quelques champs svp.",
    }
    description = forms.CharField(widget=forms.Textarea)
    somme = forms.DecimalField(widget=forms.HiddenInput(), initial=0, decimal_places=2)

    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users', [])
        self.depense = kwargs.pop('instance', None)
        super(DepenseForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs \
            .update({
                'class': 'form-control',
                'rows': '2',
            })
        if self.users:
            for u in self.users:
                self.fields['montant_depense_{user}'.format(user=u.username)] = \
                                                            forms.DecimalField(
                                                                    min_value=0,
                                                                    initial=0,
                                                                    decimal_places=2,
                                                                    label='Montant dépensé'
                                                            )
                self.fields['montant_depense_{user}'.format(user=u.username)].widget.attrs \
                    .update({
                        'class': 'form-control',
                    })
                self.fields['montant_utilise_{user}'.format(user=u.username)] = \
                                                    forms.DecimalField(
                                                                    min_value=0,
                                                                    initial=0,
                                                                    decimal_places=2,
                                                                    label='Montant utilisé'
                                                    )
                self.fields['montant_utilise_{user}'.format(user=u.username)].widget.attrs \
                    .update({
                        'class': 'form-control',
                    })
        if self.depense:
            for s_c in self.depense.spammeurconsommateur_set.all():
                print(s_c.user.username)
                self.fields['montant_depense_{user}'.format(user=s_c.user.username)].initial = s_c.montant_depense
                self.fields['montant_utilise_{user}'.format(user=s_c.user.username)].initial = s_c.montant_utilise
            self.fields['description'].initial = self.depense.description

    def clean(self):
        somme = Decimal(0.00)
        depense = Decimal(0.00)
        for u in self.users:
            depense += self.cleaned_data.get('montant_depense_{user}'.format(user=u.username)) or 0
            somme += self.cleaned_data.get('montant_depense_{user}'.format(user=u.username)) or 0
            somme -= self.cleaned_data.get('montant_utilise_{user}'.format(user=u.username)) or 0
        if somme != Decimal(0.00):
            raise forms.ValidationError(
                self.error_messages['total_non_nul'] % str(somme),
                code='total_non_nul',
            )
        if depense == 0:
            raise forms.ValidationError(
                self.error_messages['montant_inutile'],
                code='montant_inutile',
            )
        self.cleaned_data['somme'] = somme
        return self.cleaned_data
