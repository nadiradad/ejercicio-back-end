from django.db import models
from apps.artista.models import Artista  # Importamos la relación

# Create your models here.
class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    letra = models.TextField(blank=True, null=True)
    duracion_segundos = models.IntegerField()
    fecha_lanzamiento = models.DateField(blank=True, null=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="canciones")

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"