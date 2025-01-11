from django.db import models

# Create your models here.
class Autores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(default=None)
    codigo_postal=models.IntegerField(default=None)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Resumenes(models.Model):
    titulo=models.CharField(max_length=100)
    cuerpo=models.CharField(max_length=500)
    poster=models.BooleanField()
    fecha_revision=models.DateField()
    
    def __str__(self):
        return f"{self.titulo}"

class Revisores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(default=None)
    area=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"