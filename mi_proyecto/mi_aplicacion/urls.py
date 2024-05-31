
from django.urls import path
from . import views
from mi_aplicacion.views import (
    RefugioCreate,
    RefugioDelete,
    RefugioDetail,
    RefugioList,
    RefugioUpdate,
)

app_name = "mi_aplicacion"

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about_us, name='about_us'),
    path("mascota/list", views.MascotaList, name="mascota_list"),
    path("mascota/create", views.MascotaCreate.as_view(), name="mascota_create"),
    #path("refugio/list", views.RefugioList.as_view(), name="refugio_list"),
    #path("refugio/create", views.RefugioCreate.as_view(), name="refugio_create"),
]

# VISTAS BASADAS EN CLASES

urlpatterns += [
    path("refugio/list", RefugioList.as_view(), name="refugio_list"),
    path("refugio/create", RefugioCreate.as_view(), name="refugio_create"),
    path("refugio/detail/<int:pk>", RefugioDetail.as_view(), name="refugio_detail"),
    path("refugio/update/<int:pk>", RefugioUpdate.as_view(), name="refugio_update"),
    path("refugio/delete/<int:pk>", RefugioDelete.as_view(), name="refugio_delete"),
]


