from django.db import models

# Create your models here.

class Info(models.Model):
    nombre = models.TextField(max_length=20)
    telefono = models.IntegerField()
    ciudad = models.TextField(max_length=20)
    servicio = models.TextField(max_length=100)
    breve_descripcion = models.TextField(max_length=500)
    imagen=models.ImageField(upload_to = 'imagenes/', default = 'imagenes/None/no-img.jpg')
    nro= models.IntegerField(default= 0)

    def __str__(self):
        return self.nombre