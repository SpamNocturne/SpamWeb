# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SpamAlyzer', '0004_fichiersoumis_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotScore',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('mot', models.CharField(max_length=500)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='fichiersoumis',
            old_name='date',
            new_name='date_depot',
        ),
        migrations.RemoveField(
            model_name='fichiersoumis',
            name='status',
        ),
        migrations.AddField(
            model_name='fichiersoumis',
            name='date_fichier',
            field=models.DateField(default=datetime.datetime(2015, 7, 29, 22, 39, 24, 55049, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='texte',
            field=models.CharField(null=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='utilisateurstats',
            name='nom_fb',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='motscore',
            name='user',
            field=models.ForeignKey(to='SpamAlyzer.UtilisateurStats'),
        ),
        migrations.AlterUniqueTogether(
            name='motscore',
            unique_together=set([('user', 'mot')]),
        ),
    ]
