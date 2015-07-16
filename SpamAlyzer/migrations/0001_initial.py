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
            name='FichierSoumis',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField()),
                ('fichier', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('texte', models.CharField(max_length=5000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UtilisateurStats',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nom_fb', models.CharField(max_length=250)),
                ('nb_de_messages', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='auteur',
            field=models.ForeignKey(to='SpamAlyzer.UtilisateurStats'),
        ),
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.ForeignKey(to='SpamAlyzer.FichierSoumis'),
        ),
    ]
