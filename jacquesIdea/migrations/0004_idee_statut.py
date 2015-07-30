# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jacquesIdea', '0003_auto_20150622_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='idee',
            name='statut',
            field=models.IntegerField(default=1),
        ),
    ]
