from django.db import models

# Create your models here.
class Pokemons(models.Model):
    name = models.CharField(max_length=30)
    height = models.DecimalField(max_digits=20, decimal_places=2)
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    types = models.CharField(max_length=30)
    abilities = models.CharField(max_length=100)

    def __str__(self):
        return self.name
