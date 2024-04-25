"""
URL configuration for pokedex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path

from .views import get_move_identifier, get_pokemon_identifier, get_pokemon_features, get_pokemon_type, get_item_identifier, create_user

urlpatterns = [
    path('api/moves/<int:move_id>/', get_move_identifier, name='get_move_identifier'),
    path('api/pokemon/<int:pokemon_id>/', get_pokemon_identifier, name='get_pokemon_identifier'),
    path('api/pokemon/<str:pokemon_name>/', get_pokemon_features, name='get_pokemon_features'),
    path('api/pokemon/types/<str:pokemon_name>/', get_pokemon_type, name='get_pokemon_type'),
    path('api/items/<int:item_id>/', get_item_identifier, name='get_item_identifier'),
    path('api/register/', create_user, name='create_user'),

]