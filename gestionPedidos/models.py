from django.db import models

# vamos a crear una calse por cada tabla que necesitemos

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    telefono = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre
    


class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=20, verbose_name="Sección") #el verbose_name es para cambiar el nombre q aparece en el admin sin afectar la DB.
    precio = models.IntegerField()

    def __str__(self):
        #return 'El nombre es: %s , La Sección es: %s , El precio es: %s' %(self.nombre, self.seccion, self.precio)
        return self.nombre
    

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return "Entregado: %s"%(self.entregado)
    

        