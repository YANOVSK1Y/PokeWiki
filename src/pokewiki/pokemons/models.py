from django.db import models

class Pokemons(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    height = models.DecimalField(max_digits=20, decimal_places=2)
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    types = models.CharField(max_length=30)
    abilities = models.CharField(max_length=100)
    # picture = models.FileField(upload_to='../templates/picture')
    picture_name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
