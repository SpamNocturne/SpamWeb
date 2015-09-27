from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(SpammeurConsommateur)
admin.site.register(BattleDArgent)


class SpammeurConsommateurInline(admin.StackedInline):
    model = SpammeurConsommateur
    extra = 1
    classes = ('collapse open',)
    inline_classes = ('collapse open',)


class DepenseAdmin(admin.ModelAdmin):
    inlines = [SpammeurConsommateurInline]

admin.site.register(Depense, DepenseAdmin)
