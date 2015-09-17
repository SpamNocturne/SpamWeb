# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamCompte', '0005_auto_20150916_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='battledargent',
            name='pub_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
