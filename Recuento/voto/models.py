from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Longitud', max_digits=14, decimal_places=10, default=0)

    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Lugar_de_votacion(models.Model):
    nombre = models.CharField('Nombre del lugar', max_length=128)
    capacidad = models.IntegerField('Capacidad de votantes', default=500)

class Candidato(models.Model):
    nombre = models.CharField('Nombre del candidato', max_length=25)
    distrito = models.ForeignKey(Distrito)

class Voto(models.Model):
    valido = models.BooleanField(null=False)


