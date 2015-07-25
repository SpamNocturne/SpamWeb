# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('spamConso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='consommation',
            name='consommateur',
            field=models.ForeignKey(related_name='consommations', to=settings.AUTH_USER_MODEL, related_query_name='consommation'),
        ),
        migrations.AlterField(
            model_name='consommation',
            name='description',
            field=models.CharField(blank=True, max_length=60, default=''),
        ),
        migrations.AlterField(
            model_name='consommation',
            name='type',
            field=models.CharField(choices=[('tacos', 'tacos'), ('biere', 'biere')], max_length=20),
        ),
        migrations.AddField(
            model_name='consommation',
            name='tags',
            field=models.ManyToManyField(related_query_name='tag', to='spamConso.ConsoTag', related_name='tags'),
        ),
    ]
