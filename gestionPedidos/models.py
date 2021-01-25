from django.db import models

# vamos a crear una calse por cada tabla que necesitemos

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    telefono = models.CharField(max_length=10)


class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

        