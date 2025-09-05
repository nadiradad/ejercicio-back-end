from django.urls import path
from . import views

urlpatterns = [
    path("canciones/", views.lista_canciones, name="lista_canciones"),
]