from django.contrib import admin

# Register your models here.
from SpamAlyzer import models

admin.site.register(models.UtilisateurStats)
admin.site.register(models.FichierSoumis)
admin.site.register(models.Message)
admin.site.register(models.MotScore)