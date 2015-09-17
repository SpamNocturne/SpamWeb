# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SpamCompte', '0006_battledargent_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='depense',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='depense',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 9, 17, 22, 38, 21, 48142, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
