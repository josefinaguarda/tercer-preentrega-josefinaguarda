from django.db import models
from django.utils import timezone

class Mascota(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Macho'), ('H', 'Hembra')])
    descripcion = models.TextField()
    refugio = models.ForeignKey('Refugio', on_delete=models.CASCADE, related_name='mascotas', null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
class Refugio(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    #mascota_id= models.ManyToManyField(Mascota, related_name='refugios', blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
    
# esta clase ya no es necesaria, ya que cree la app adopcion.
class Adoptante(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    mascota_id= models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True, blank=True)
    
