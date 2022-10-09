from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Persona(models.Model):
  tipo_documento = models.CharField(max_length=255)
  documento = models.CharField(max_length=255)
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  hobbie = models.CharField(max_length=255)

  def __str__(self):
    return self.tipo_documento, self.documento, self.nombre, self.apellido, self.hobbie
