from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemons

# Create your views here.
def home_view(request, *args, **kwargs):
    pokemons = Pokemons.objects.all()
    return render(request, "home.html", {'all': Pokemons})


def pokemons_view(request, *args, **kwargs):
    return render(request, 'pokemons.html', {})


def about_view(request, *args, **kwargs):
    context = {
            "email": "Exaple@gmail.com",
            "phone":+380777777777,
    }
    return render(request, "about.html", context)
