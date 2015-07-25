from django.contrib import admin
from .models import Log, FirstUnseenLog

# Register your models here.
admin.site.register(Log)
admin.site.register(FirstUnseenLog)