# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('spamusic', '0002_auto_20150711_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentialsyoutubemodel',
            name='id',
            field=models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
