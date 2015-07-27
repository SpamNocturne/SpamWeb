# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


<<<<<<< HEAD
=======
def content_file_name(instance, filename):
    return '/'.join(['avatars', instance.user.username, filename])


>>>>>>> 0a362510ac2175dad2071591e7baf7debc9d6dbe
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_de_naissance = models.DateField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Le numéro de téléphone doit être composé de 10 chiffres.")
    telephone = models.CharField(max_length=10, validators=[phone_regex], blank=True, null=True)  # validators should be a list
<<<<<<< HEAD
    avatar = models.ImageField(upload_to="uploads", blank=True, null=True)
=======
    avatar = models.ImageField(upload_to=content_file_name, blank=True, null=True)
>>>>>>> 0a362510ac2175dad2071591e7baf7debc9d6dbe
    # TODO null=True et image par défaut


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
