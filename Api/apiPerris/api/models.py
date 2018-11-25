from django.db import models

# Create your models here.

class Perro(models.Model):
    estado_opc = (
        ('AD', 'Adoptado'),
        ('RE', 'Rescatado'),
        ('DI', 'Disponible'),
    )
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=2, choices=estado_opc)
    def __str__(self):
        return self.nombre