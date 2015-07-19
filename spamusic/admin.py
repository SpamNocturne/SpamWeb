from django.contrib import admin
from .models import CredentialsYoutubeModel

class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsYoutubeModel, CredentialsAdmin)
