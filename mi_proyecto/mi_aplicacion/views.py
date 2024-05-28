#from django.shortcuts import render
#from django.urls import reverse_lazy
#from django.views.generic import CreateView, ListView
from .models import Mascota
from . import models, forms

from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from mi_aplicacion.forms import RefugioForm
from mi_aplicacion.models import Refugio


def index(request):
    return render(request, "mi_aplicacion/index.html")

def MascotaList(request):
    # Filtra las mascotas que no están asociadas a ningún adoptante
  mascotas = Mascota.objects.filter(adoptante__isnull=True)
  return render(request, 'mi_aplicacion/mascota_list.html', {'mascotas': mascotas})
 
 
#def MascotaList(request):
    # Filtra las mascotas que no están asociadas a ningún adoptante y que tienen un refugio asociado
 # mascotas = Mascota.objects.filter(adoptante__isnull=True, refugio__isnull=False)
 # return render(request, 'mi_aplicacion/mascota_list.html', {'mascotas': mascotas})


class MascotaCreate(CreateView):
    model = models.Mascota
    form_class = forms.MascotaForm
    success_url = reverse_lazy("mi_aplicacion:mascota_list")
    
#class RefugioList(ListView):
 #   model = models.Refugio


#class RefugioCreate(CreateView):
 #   model = models.Refugio
  #  form_class = forms.RefugioForm
   # success_url = reverse_lazy("mi_aplicacion:refugio_list")  

class RefugioList(ListView):
    model = Refugio

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Refugio.objects.filter(nombre__icontains=busqueda)
        return queryset


class RefugioCreate(CreateView):
    model = Refugio
    form_class = RefugioForm
    success_url = reverse_lazy("mi_aplicacion:refugio_list")


class RefugioDetail(DetailView):
    model = Refugio


class RefugioUpdate(UpdateView):
    model = Refugio
    form_class = RefugioForm
    success_url = reverse_lazy("mi_aplicacioin:refugio_list")
    
class RefugioDelete(DeleteView):
    model = Refugio
    success_url = reverse_lazy("mi_aplicacion:refugio_list")


