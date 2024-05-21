from django.contrib import admin

from . import models 

admin.site.register(models.Mascota)
admin.site.register(models.Refugio)
admin.site.register(models.Adoptante)


