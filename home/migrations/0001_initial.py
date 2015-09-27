# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstUnseenLog',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.CharField(max_length=255)),
                ('app', models.CharField(max_length=100)),
                ('log_type', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='logs', related_query_name='log')),
            ],
        ),
        migrations.AddField(
            model_name='firstunseenlog',
            name='log',
            field=models.ForeignKey(to='home.Log', related_name='first_unseen_logs', null=True, blank=True, related_query_name='first_unseen_log'),
        ),
    ]
