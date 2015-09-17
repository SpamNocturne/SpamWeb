# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SpamCompte', '0003_battledargent_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battledargent',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
