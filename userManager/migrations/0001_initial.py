# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userManager.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('telephone', models.CharField(validators=[django.core.validators.RegexValidator(message='Le numéro de téléphone doit être composé de 10 chiffres.', regex='^\\d{10}$')], blank=True, max_length=10, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=userManager.models.content_file_name)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
