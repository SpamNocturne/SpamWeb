from django.contrib import admin

# Register your models here.
from .models import Idee, Commentaire, Vote

admin.site.register(Idee)
admin.site.register(Commentaire)
admin.site.register(Vote)