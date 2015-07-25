# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userManager.models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0006_auto_20150720_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=userManager.models.content_file_name),
        ),
    ]
