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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SpammeurConsommateur',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('montant_depense', models.PositiveIntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='mes_transactions')),
            ],
        ),
        migrations.AddField(
            model_name='depense',
            name='beneficiaires',
            field=models.ManyToManyField(to='SpamCompte.SpammeurConsommateur', related_name='mes_achats_que_je_dois_rembourser'),
        ),
        migrations.AddField(
            model_name='depense',
            name='my_son_my_battle',
            field=models.ForeignKey(to='SpamCompte.BattleDArgent'),
        ),
        migrations.AddField(
            model_name='depense',
            name='payeurs',
            field=models.ManyToManyField(to='SpamCompte.SpammeurConsommateur', related_name='mes_depenses_pour_des_spammeurs'),
        ),
    ]
