# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamCompte', '0004_auto_20150927_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battledargent',
            name='nom',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
