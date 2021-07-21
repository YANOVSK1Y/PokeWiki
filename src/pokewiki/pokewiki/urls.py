"""pokewiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pokemons.views import home_view, about_view, pokemons_view


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('pokemons/', pokemons_view, name='pokemons'),
    path('about/', about_view, name='about')
]

# for i in range(50):
#     if os.path.exists(str(i[0])+'.png'):
#         Pokemons.objects.create(id=str(data[i][0])+'.png', name=str(data[i][1]), height=data[i][2], weight=data[i][3], types=str(data[i][4]), abilities=str(data[i][5]), picture_status=True)
#     else:
#         Pokemons.objects.create(id=str(data[i][0])+'.png', name=str(data[i][1]), height=data[i][2], weight=data[i][3], types=str(data[i][4]), abilities=str(data[i][5]), picture_status=False)
