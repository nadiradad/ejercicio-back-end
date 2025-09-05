from django.shortcuts import render
from .models import Artista
# Create your views here.

def lista_artistas(request):
    artistas = Artista.objects.all()  # Consulta todos los artistas
    return render(request, "artista/lista.html", {"artistas": artistas})