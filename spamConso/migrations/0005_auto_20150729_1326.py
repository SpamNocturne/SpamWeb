# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spamConso', '0004_auto_20150725_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consommation',
            name='tags',
            field=models.CharField(default='', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='consotag',
            name='value',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
