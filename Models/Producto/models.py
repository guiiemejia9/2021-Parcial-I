

from django.db import models
from Models.Marca.models import Marca
from Models.Categoria.models import Categoria


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=75)
    descripcion=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=9, decimal_places=2)
    # relacion de uno a muchos con tabla marca
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=False, blank=False)
    # relacion de uno a muchos con tabla categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)

