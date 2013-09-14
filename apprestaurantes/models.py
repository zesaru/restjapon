from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nombre = models.CharField(max_length = 140)
    direccion = models.CharField(max_length = 140)
    telefono = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 140, blank =True,)
    facebook = models.URLField(max_length = 140, blank =True,)
    twitter = models.URLField(max_length = 140, blank =True,)
    homepage = models.URLField(max_length = 140, blank =True,)