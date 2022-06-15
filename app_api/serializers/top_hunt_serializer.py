from rest_framework import serializers
from app_api.models import Hunt
from app_api.serializers.game_serializer import EmbedGameSerializer
from app_api.serializers.method_serializer import EmbedMethodSerializer
from app_api.serializers.trainer_serializers import HuntTrainerSerializer
from app_api.serializers.pokemon_serializer import EmbedPokemonSerializer


class HuntSerializer(serializers.ModelSerializer):
    trainer = HuntTrainerSerializer(many=False)
    pokemon = EmbedPokemonSerializer(many=False)
    game = EmbedGameSerializer(many=False)
    method = EmbedMethodSerializer(many=False)
    class Meta:
        model = Hunt
        fields = ('id', 'trainer', 'pokemon', 'encounters', 'completed', 'method', 'game', 'shiny_charm', 'date_started', 'date_completed')