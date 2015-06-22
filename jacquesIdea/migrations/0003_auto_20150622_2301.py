# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jacquesIdea', '0002_auto_20150615_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idee',
            name='titre',
            field=models.CharField(max_length=150),
        ),
    ]
