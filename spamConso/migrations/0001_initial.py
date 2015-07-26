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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('type', models.CharField(max_length=60, choices=[('tacos', 'tacos'), ('biere', 'biere')])),
                ('description', models.CharField(max_length=60)),
                ('conso_date', models.DateTimeField()),
                ('consommateur', models.ForeignKey(related_name='Consommation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
