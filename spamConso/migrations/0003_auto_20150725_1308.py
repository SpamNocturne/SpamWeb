# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spamConso', '0002_auto_20150725_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consommation',
            name='tags',
        ),
        migrations.AddField(
            model_name='consommation',
            name='tags',
            field=models.CharField(default='', choices=[('tacos', 'Tacos'), ('biere', 'Biere')], max_length=255),
        ),
        migrations.AlterField(
            model_name='consommation',
            name='type',
            field=models.CharField(choices=[('tacos', 'Tacos'), ('biere', 'Biere')], max_length=20),
        ),
    ]
