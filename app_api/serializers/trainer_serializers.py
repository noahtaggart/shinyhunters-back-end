from rest_framework import serializers
from app_api.models import Trainer
from django.contrib.auth.models import User


class EmbedUserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model= User
        fields= ('id', 'first_name', 'last_name', 'username' )
    
    
class EmbedTrainerSerializer(serializers.ModelSerializer):
    user = EmbedUserSerializer(many=False)
    
    class Meta:
        model = Trainer
        fields = ('id', 'bio', 'user')
        depth = 1