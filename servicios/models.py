from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    duracion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Create your models here.
