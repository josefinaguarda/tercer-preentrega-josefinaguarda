from django import forms
from .models import Mascota, Refugio, Adoptante

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'edad', 'sexo', 'descripcion']

class RefugioForm(forms.ModelForm):
    class Meta:
        model = Refugio
        fields = ['nombre', 'direccion', 'telefono']

class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante
        fields = ['nombre', 'direccion', 'telefono', 'mascota_preferida']

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)