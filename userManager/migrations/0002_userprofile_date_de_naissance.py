# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_de_naissance',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 21, 3, 49, 977666, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
