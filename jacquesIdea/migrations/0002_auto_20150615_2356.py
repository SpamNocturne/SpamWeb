# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jacquesIdea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 21, 56, 10, 679858, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('auteur', 'idee')]),
        ),
    ]
