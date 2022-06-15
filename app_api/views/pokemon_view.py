from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from app_api import serializers
from app_api.models import Hunt, Following, Trainer, Pokemon
from app_api.models.game import Game
from app_api.models.method import Method
from app_api.serializers import HuntSerializer
from rest_framework import status
from django.core.exceptions import ValidationError

from app_api.serializers.pokemon_serializer import EmbedPokemonSerializer


class PokemonView(ViewSet):
    
    def list(self, request):
        pokemon = Pokemon.objects.filter(id__lte=898)
        
        serializer = EmbedPokemonSerializer(pokemon, many=True)
        return Response(serializer.data)