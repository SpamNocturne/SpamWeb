# -*- coding: utf-8 -*-

import datetime
from django.contrib.auth.models import User
import json
from django.db import models
from django.utils import timezone


class ConsoTag(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return 'Tag : %s (%s)' % (self.name, self.value)


class Consommation(models.Model):
    CONSO_CHOICES = (
        ('tacos', 'Tacos'),
        ('biere', 'Biere')
    )
    type = models.CharField(max_length=20, choices=CONSO_CHOICES)
    description = models.CharField(max_length=60, blank=True, default="")
    tags = models.CharField(max_length=255, blank=True, default="")
    conso_date = models.DateTimeField()
    consommateur = models.ForeignKey(User, related_name='consommations', related_query_name="consommation")

    def __str__(self):
        return "%s a consommé %s le %s - Tag %s" % (
        self.type, self.consommateur.username, str(self.conso_date.strftime("%d/%m/%Y %H:%M:%S")), str(self.tags))

    @property
    def get_tags_as_dict(self):
        if self.tags:
            return json.loads(self.tags)
        return dict()