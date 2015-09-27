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
            name='BattleDArgent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(null=True, blank=True)),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('my_son_my_battle', models.ForeignKey(to='SpamCompte.BattleDArgent')),
            ],
        ),
        migrations.CreateModel(
            name='SpammeurConsommateur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('montant_depense', models.IntegerField(default=0)),
                ('depense_pour_laquelle_on_contribue', models.ForeignKey(to='SpamCompte.Depense')),
                ('user', models.ForeignKey(related_name='mes_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
