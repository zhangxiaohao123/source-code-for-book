from django.contrib import admin
from . import models

class authorityadmin(admin.ModelAdmin):
    list_display = ('codename','url','name')


# Register your models here.
admin.site.register(models.authority,authorityadmin)
