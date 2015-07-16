# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamAlyzer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichiersoumis',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
