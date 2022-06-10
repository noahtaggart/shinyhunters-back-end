from rest_framework import serializers
from app_api.models import Trainer
from django.contrib.auth.models import User

from app_api.serializers.hunt_serializers import EmbedHuntSerializer





class EmbedUserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model= User
        fields= ('id', 'first_name', 'last_name', 'username' )
    
    
class EmbedTrainerSerializer(serializers.ModelSerializer):
    user = EmbedUserSerializer(many=False)
    recent_completed_hunt = EmbedHuntSerializer()
    
    class Meta:
        model = Trainer
        fields = ('id', 'bio', 'user', 'recent_completed_hunt')
        depth = 1

