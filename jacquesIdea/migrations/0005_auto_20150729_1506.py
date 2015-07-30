# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jacquesIdea', '0004_idee_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idee',
            name='statut',
            field=models.IntegerField(default=0),
        ),
    ]
