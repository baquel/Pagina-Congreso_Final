from django.db import models

# Create your models here.
class Autores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(default=None)
    codigo_postal=models.IntegerField(default=None)

class Resumenes(models.Model):
    titulo=models.CharField(max_length=100)
    cuerpo=models.CharField(max_length=500)
    poster=models.BooleanField()
    fecha_revision=models.DateField()

class Revisores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(default=None)
    area=models.CharField(max_length=20)