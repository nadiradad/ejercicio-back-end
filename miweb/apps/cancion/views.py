from django.shortcuts import render
from .models import Cancion
# Create your views here.

def lista_canciones(request):
    canciones = Cancion.objects.all()  # Consulta todas las canciones
    return render(request, "cancion/lista.html", {"canciones": canciones})
