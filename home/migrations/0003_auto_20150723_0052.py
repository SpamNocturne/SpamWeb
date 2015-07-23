# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_lastseenlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastseenlog',
            name='log',
            field=models.ForeignKey(related_name='last_seen_logs', null=True, to='home.Log', related_query_name='last_seen_log'),
        ),
    ]
