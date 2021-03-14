from django.db import models

# Create your models here.


# Create your models here.
class Categoria(models.Model):
    id= models.AutoField(primary_key = True)
    nombre= models.CharField(max_length=75)

# retornar campos para input Select
    def __str__(self):
        return self.nombre