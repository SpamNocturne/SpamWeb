# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spamConso', '0003_auto_20150725_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='consotag',
            name='value',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consommation',
            name='tags',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.AlterField(
            model_name='consotag',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
