from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    es_solista = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre