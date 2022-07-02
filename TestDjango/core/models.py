from django.db import models

# Create your models here.

class stock(models.Model):
    cod = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)


class compra(models.Model):
    compra = models.IntegerField(primary_key=True)
    producto = models.CharField(max_length=50)
    precio = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=30)


