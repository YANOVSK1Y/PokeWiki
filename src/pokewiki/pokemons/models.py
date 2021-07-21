from django.db import models

class Pokemons(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    height = models.DecimalField(max_digits=20, decimal_places=2)
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    types = models.CharField(max_length=30)
    abilities = models.CharField(max_length=100)
    picture_status = models.BooleanField(default=False)


    def __str__(self):
        return str(str(self.id) + '-' +  str(self.name) + '-' + str(self.picture_status))
