from django.contrib import admin

from . import models 


class MascotaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "edad",
        "sexo",
        "descripcion",
        "refugio",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    list_filter = ("refugio",)
    date_hierarchy = "fecha_actualizacion"
    
    

admin.site.register(models.Mascota, MascotaAdmin)
admin.site.register(models.Refugio)
admin.site.register(models.Adoptante)


