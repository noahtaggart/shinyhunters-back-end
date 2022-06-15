from rest_framework import serializers
from app_api.models import Hunt
from app_api.serializers.game_serializer import EmbedGameSerializer
from app_api.serializers.pokemon_serializer import EmbedPokemonSerializer

        
class EmbedHuntSerializer(serializers.ModelSerializer):
    pokemon = EmbedPokemonSerializer(many=False)
    game = EmbedGameSerializer(many=False)
    class Meta:
        model = Hunt
        fields = ('id', 'pokemon', 'game', 'encounters', 'completed')

