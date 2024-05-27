from django.urls import path
# from . import views
from core.views import index

app_name = "core"

urlpatterns = [
    #path("", views.home, name="home"),
    path("", index, name="index"),
]
