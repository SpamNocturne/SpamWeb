# -*- coding: utf-8 -*-

import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Consommation(models.Model):
    CONSO_CHOICES = ( ('tacos', 'tacos'),
                      ('biere', 'biere'))
    type = models.CharField(max_length=60, choices = CONSO_CHOICES)
    description = models.CharField(max_length=60)
    conso_date = models.DateTimeField()
    consommateur = models.ForeignKey(User, related_name='Consommation')


    def __str__(self):
        return self.type
