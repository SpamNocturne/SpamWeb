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
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('commentaire_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Idee',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('titre', models.CharField(max_length=150)),
                ('idee_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('statut', models.IntegerField(default=0)),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='idees')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('valeur', models.IntegerField(default=0)),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('idee', models.ForeignKey(to='jacquesIdea.Idee')),
            ],
        ),
        migrations.AddField(
            model_name='idee',
            name='votants',
            field=models.ManyToManyField(through='jacquesIdea.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='idee',
            field=models.ForeignKey(to='jacquesIdea.Idee'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('auteur', 'idee')]),
        ),
    ]
