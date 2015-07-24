from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Log(models.Model):
    text = models.CharField(max_length=255)
    app = models.CharField(max_length=100)
    log_type = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="logs", related_query_name="log")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class FirstUnseenLog(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    log = models.ForeignKey(Log, related_name="first_unseen_logs", related_query_name="first_unseen_log", null=True, blank=True)
