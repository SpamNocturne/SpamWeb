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
            name='FirstUnseenLog',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('log', models.ForeignKey(related_name='first_unseen_logs', null=True, blank=True, related_query_name='first_unseen_log', to='home.Log')),
            ],
        ),
    ]
