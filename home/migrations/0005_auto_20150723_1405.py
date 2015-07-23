# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('home', '0004_auto_20150723_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstUnseenLog',
            fields=[
                ('user', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('log', models.ForeignKey(to='home.Log', related_query_name='first_unseen_log', related_name='first_unseen_logs', blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='lastseenlog',
            name='log',
        ),
        migrations.RemoveField(
            model_name='lastseenlog',
            name='user',
        ),
        migrations.DeleteModel(
            name='LastSeenLog',
        ),
    ]
