from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_de_naissance = models.DateField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Le numéro de téléphone doit être composé de 10 chiffres.")
    telephone = models.CharField(max_length=10, validators=[phone_regex], blank=True, null=True)  # validators should be a list
    avatar = models.ImageField(upload_to="uploads", blank=True, null=True)
    # TODO null=True et image par défaut
