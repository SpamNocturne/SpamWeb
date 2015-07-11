from django.contrib import admin
from .models import CredentialsModel

class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)
