from django.urls import path
from . import views

urlpatterns = [
    path("artistas/", views.lista_artistas, name="lista_artistas"),
]