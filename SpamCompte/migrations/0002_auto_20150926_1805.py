# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SpamCompte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spammeurconsommateur',
            name='depense_pour_laquelle_on_contribue',
            field=models.ForeignKey(to='SpamCompte.Depense', null=True),
        ),
    ]
