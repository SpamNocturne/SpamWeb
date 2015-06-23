# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0003_auto_20150622_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='image_profil',
            new_name='avatar',
        ),
    ]
