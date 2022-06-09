from rest_framework import serializers
from app_api.models import Game

class EmbedGameSerializer(serializers.ModelSerializer):
    """JSON serializer for embedded game"""
    class Meta:
        model=Game
        fields=('id', 'title',)