    
from django import forms
from . import models

class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = "__all__"
        
#class RefugioForm(forms.ModelForm):
 #   class Meta:
  #      model = models.Refugio
   #     fields = "__all__"
   

class RefugioForm(forms.ModelForm):
    class Meta:
        model = models.Refugio
        fields = ["nombre", "direccion", "telefono"]
