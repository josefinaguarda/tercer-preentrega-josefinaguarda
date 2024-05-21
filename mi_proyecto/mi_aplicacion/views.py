 
# from django.shortcuts import render, redirect
# from .forms import MascotaForm, RefugioForm, AdoptanteForm

# def home(request):
  #  return render(request, "mi_aplicacion/index.html")

#def formulario_mascota(request):
 #   if request.method == 'POST':
   #     form = MascotaForm(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      return redirect("formulario_mascota")  
       # form = MascotaForm()
   # return render(request, "mi_aplicacion/mascotaform.html", {'form': form})

#def formulario_refugio(request):
 #   if request.method == 'POST':
  #      form = RefugioForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect("formulario_refugio")  
      #  form = RefugioForm()
    #return render(request, "mi_aplicacion/refugioform.html", {'form': form})

#def formulario_adoptante(request):
 #   if request.method == 'POST':
  #      form = AdoptanteForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect("formulario_adoptante")  
      #  form = AdoptanteForm()
   # return render(request, "mi_aplicacion/adoptanteform.html", {'form': form})
   
   
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms


def home(request):
    return render(request, "mi_aplicacion/index.html")


class MascotaList(ListView):
    model = models.Mascota


class MascotaCreate(CreateView):
    model = models.Mascota
    form_class = forms.MascotaForm
    success_url = reverse_lazy("mi_aplicacion:mascota_list")