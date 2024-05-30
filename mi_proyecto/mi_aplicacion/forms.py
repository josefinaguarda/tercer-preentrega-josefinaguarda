from django import forms
from . import models

#class MascotaForm(forms.ModelForm):
#    class Meta:
#        model = models.Mascota
#        fields = "__all__"
        
class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "edad": forms.TextInput(attrs={"class": "form-control"}),
            "sexo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }      
                
#class RefugioForm(forms.ModelForm):
#    class Meta:
#        model = models.Refugio
#        fields = ["nombre", "direccion", "telefono"]
        
class RefugioForm(forms.ModelForm):
    class Meta:
        model = models.Refugio
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "mascota_id": forms.Select(attrs={"class": "form-control"})
        }   
