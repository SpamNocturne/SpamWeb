# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamAlyzer', '0003_auto_20150707_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichiersoumis',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
