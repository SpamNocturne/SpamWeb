# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamCompte', '0002_auto_20150926_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spammeurconsommateur',
            name='depense_pour_laquelle_on_contribue',
            field=models.ForeignKey(blank=True, null=True, to='SpamCompte.Depense'),
        ),
    ]
