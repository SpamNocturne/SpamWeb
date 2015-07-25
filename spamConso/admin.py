from django.contrib import admin

# Register your models here.
from .models import Consommation, ConsoTag
admin.site.register(Consommation)
admin.site.register(ConsoTag)