from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()

    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificaicon = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.titulo
