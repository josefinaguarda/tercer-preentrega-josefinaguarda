from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Macho'), ('H', 'Hembra')])
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Refugio(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

class Adoptante(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    mascota_id= models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True, blank=True)
