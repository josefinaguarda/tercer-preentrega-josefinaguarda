from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


class Adoptante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="adoptante")
    celular = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self) -> str:
        return self.usuario.username

class Adopcion(models.Model):  # cada adoptante tendra una adopcion. 
    adoptante = models.ForeignKey(Adoptante, on_delete=models.SET_NULL, null=True, blank=True)
    mascota = models.ForeignKey("mi_aplicacion.Mascota", on_delete=models.DO_NOTHING)
    fecha_adopcion = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:  # da un orden a los campos. 
        ordering = ("-fecha_adopcion",)

    def clean(self):
        # Verificar si esta mascota ya ha sido adoptada
        if Adopcion.objects.filter(mascota=self.mascota).exists():
            raise ValidationError("Esta mascota ya ha sido adoptada")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # No se necesita asignar el adoptante a la mascota directamente
        # La relación se puede consultar a través del modelo Adopcion
        
        
        
