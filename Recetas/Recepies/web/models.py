

from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo', default='')
    descripcion = models.TextField(max_length=300, verbose_name='Descripcion', default='')
    duracion = models.IntegerField(verbose_name='Duracion')

    def __str__(self):
        return self.titulo


  
