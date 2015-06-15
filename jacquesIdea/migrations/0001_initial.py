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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('commentaire_text', models.TextField()),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Idee',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('idee_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('auteur', models.ForeignKey(related_name='idees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
    ]
