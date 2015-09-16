# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamAlyzer', '0005_auto_20150730_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateurstats',
            name='nb_de_messages',
        ),
    ]
