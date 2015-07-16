# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamAlyzer', '0002_auto_20150707_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichiersoumis',
            name='fichier',
            field=models.FileField(upload_to='uploads/SpamAlyzer/%Y-%m-%d/'),
        ),
    ]
