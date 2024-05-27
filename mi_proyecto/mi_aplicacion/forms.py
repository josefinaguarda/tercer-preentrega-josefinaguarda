# from django import forms
# from .models import Mascota, Refugio, Adoptante

# class MascotaForm(forms.ModelForm):
  #  class Meta:
   #     model = Mascota
    #    fields = ['nombre', 'edad', 'sexo', 'descripcion']  

# class RefugioForm(forms.ModelForm):
  #  class Meta:
   #     model = Refugio
    #    fields = ['nombre', 'direccion', 'telefono'] 
# class AdoptanteForm(forms.ModelForm):
  #  class Meta:
   #     model = Adoptante
    #    fields = ['nombre', 'direccion', 'telefono', 'mascota_id']  
    
from django import forms
from . import models

class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = "__all__"
        
class RefugioForm(forms.ModelForm):
    class Meta:
        model = models.Refugio
        fields = "__all__"