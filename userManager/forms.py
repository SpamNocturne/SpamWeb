# coding: utf8
from django import forms

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Pseudo", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(ConnexionForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': "Pseudo",
                'class': 'form-control'
            })
        self.fields['password'].widget.attrs\
            .update({
                'placeholder': "Mot de passe",
                'class': 'form-control'
            })


class InscriptionForm(forms.Form):
    error_messages = {
        'password_mismatch': "Les deux mots de passe ne correspondent pas.",
        'taken_username': "Ce pseudo est déjà pris.",
        'taken_email': "Cet email est déjà utilisé."
    }

    username = forms.CharField(label="Pseudo", max_length=30)
    first_name = forms.CharField(label="Prénom", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)
    email = forms.EmailField(label="Adresse E-mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Répétez le mot de passe", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(InscriptionForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': "Pseudo",
                'class': 'form-control'
            })
        self.fields['first_name'].widget.attrs\
            .update({
                'placeholder': "Prénom",
                'class': 'form-control'
            })
        self.fields['last_name'].widget.attrs\
            .update({
                'placeholder': "Nom",
                'class': 'form-control'
            })
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': "E-mail",
                'class': 'form-control'
            })
        self.fields['password'].widget.attrs\
            .update({
                'placeholder': "Mot de passe",
                'class': 'form-control'
            })
        self.fields['password2'].widget.attrs\
            .update({
                'placeholder': "Répétition",
                'class': 'form-control'
            })

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username):
                raise forms.ValidationError(
                    self.error_messages['taken_username'],
                    code='taken_username',
                )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email):
                raise forms.ValidationError(
                    self.error_messages['taken_email'],
                    code='taken_email',
                )
        return email


class ChangeMdpForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangeMdpForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs\
            .update({
                'placeholder': "Ancien mot de passe",
                'class': 'form-control'
            })
        self.fields['new_password1'].widget.attrs\
            .update({
                'placeholder': "Nouveau mot de passe",
                'class': 'form-control'
            })
        self.fields['new_password2'].widget.attrs\
            .update({
                'placeholder': "Repetition",
                'class': 'form-control'
            })
