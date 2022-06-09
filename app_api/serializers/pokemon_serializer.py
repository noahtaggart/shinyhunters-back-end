from rest_framework import serializers
from app_api.models import Pokemon

class EmbedPokemonSerializer(serializers.ModelSerializer):
    """JSON serializer for embedded pokemon"""
    class Meta:
        model=Pokemon
        fields=('id', 'name', 'default_sprite', 'female_sprite')