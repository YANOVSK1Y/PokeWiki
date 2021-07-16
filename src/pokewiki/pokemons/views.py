from django.shortcuts import render
import os
# Create your views here.
from .models import Pokemons


folder = "/home/drew/Python_Projects/PokeWiki/src/templates/pictures"
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def pokemons_view(request, *args, **kwargs):
    pokemons = Pokemons.objects.all()
    image_counter = 1118
    return render(request, 'pokemons.html', {"all": pokemons,
    "image_folder": folder})


def about_view(request, *args, **kwargs):
    context = {
            "email": "Exaple@gmail.com",
            "phone":+380777777777,
    }
    return render(request, "about.html", context)
