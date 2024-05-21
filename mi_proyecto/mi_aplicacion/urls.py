
# from django.urls import path
# from . import views

# app_name= "MascotApp"

# urlpatterns = [
  #  path('', views.index, name='index'),
   # path('mascota/', views.formulario_mascota, name='formulario_mascota'),
   # path('refugio/', views.formulario_refugio, name='formulario_refugio'),
   # path('adoptante/', views.formulario_adoptante, name='formulario_adoptante'),
# ]

from django.urls import path
from . import views

app_name = "mi_aplicacion"

urlpatterns = [
    path("", views.home, name="home"),
    path("mascota/list", views.MascotaList.as_view(), name="mascota_list"),
    path("mascota/create", views.MascotaCreate.as_view(), name="mascota_create"),
]
