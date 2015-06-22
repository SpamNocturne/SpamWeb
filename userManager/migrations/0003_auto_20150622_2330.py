# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0002_userprofile_date_de_naissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_profil',
            field=models.ImageField(upload_to='uploads', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\d{10}$', message='Le numéro de téléphone doit être composé de 10 chiffres.')], blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_de_naissance',
            field=models.DateField(blank=True),
        ),
    ]
