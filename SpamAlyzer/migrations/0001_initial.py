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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_depot', models.DateField(auto_now_add=True)),
                ('date_fichier', models.DateField()),
                ('fichier', models.FileField(upload_to='uploads/SpamAlyzer/%Y-%m-%d/')),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('texte', models.CharField(null=True, max_length=5000)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MotScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('mot', models.CharField(max_length=500)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UtilisateurStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom_fb', models.CharField(unique=True, max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='motscore',
            name='user',
            field=models.ForeignKey(to='SpamAlyzer.UtilisateurStats'),
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
        migrations.AlterUniqueTogether(
            name='motscore',
            unique_together=set([('user', 'mot')]),
        ),
    ]
