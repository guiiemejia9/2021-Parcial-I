

# Create your models here.
from django.db import models

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=75)
    hecho=models.CharField(max_length=75)

    def __str__(self):
        return self.nombre + " " + self.hecho

