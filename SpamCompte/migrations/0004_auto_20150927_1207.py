# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('SpamCompte', '0003_auto_20150926_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='spammeurconsommateur',
            name='montant_utilise',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
        migrations.AlterField(
            model_name='spammeurconsommateur',
            name='montant_depense',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]
