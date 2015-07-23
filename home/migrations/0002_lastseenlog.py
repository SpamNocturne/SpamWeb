# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastSeenLog',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('log', models.ForeignKey(related_query_name='last_seen_log', to='home.Log', related_name='last_seen_logs')),
            ],
        ),
    ]
