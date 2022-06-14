from rest_framework import serializers
from app_api.models import Method

class EmbedMethodSerializer(serializers.ModelSerializer):
    """JSON serializer for embedded method"""
    class Meta:
        model=Method
        fields=('id', 'name', 'default_odds_fraction', 'shiny_charm_odds_fraction')