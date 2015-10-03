# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consommation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=20, choices=[('tacos', 'Tacos'), ('biere', 'Biere')])),
                ('description', models.CharField(default='', max_length=60, blank=True)),
                ('tags', models.CharField(default='', max_length=255, blank=True)),
                ('conso_date', models.DateTimeField()),
                ('consommateur', models.ForeignKey(related_name='consommations', to=settings.AUTH_USER_MODEL, related_query_name='consommation')),
            ],
        ),
        migrations.CreateModel(
            name='ConsoTag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
