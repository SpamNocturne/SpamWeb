# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0004_auto_20150623_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='uploads', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_de_naissance',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Le numéro de téléphone doit être composé de 10 chiffres.', regex='^\\d{10}$')], null=True, max_length=10, blank=True),
        ),
    ]
