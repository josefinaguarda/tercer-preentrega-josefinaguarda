from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Adopcion de Mascotas"


class AdopcionAdmin(admin.ModelAdmin):
    list_display = (
        "adoptante",
        "mascota",
        "fecha_adopcion",
    )
    list_display_links = ("mascota",)
    search_fields = ("mascota.nombre", "adoptante")
    list_filter = ("adoptante",)
    date_hierarchy = "fecha_adopcion"


admin.site.register(models.Adoptante)
admin.site.register(models.Adopcion, AdopcionAdmin)
