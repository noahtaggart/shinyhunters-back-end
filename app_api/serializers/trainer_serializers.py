from requests import request
from rest_framework import serializers
from app_api.models import Trainer
from django.contrib.auth.models import User
from app_api.models.following import Following
from app_api.models.photo import Photo

from app_api.serializers.hunt_serializers import EmbedHuntSerializer
from app_api.views.photo_view import PhotoSerializer





class EmbedUserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model= User
        fields= ('id', 'first_name', 'last_name', 'username' )
    
    
class EmbedTrainerSerializer(serializers.ModelSerializer):
    user = EmbedUserSerializer(many=False)
    recent_completed_hunt = EmbedHuntSerializer()
   
    
    profileImageUrl = serializers.SerializerMethodField()
    def get_profileImageUrl(self, obj):
        photo = PhotoSerializer(Photo.objects.filter(trainer=obj).last())
        return photo.data
    
    class Meta:
        model = Trainer
        fields = ('id', 'bio', 'user', 'recent_completed_hunt', 'profileImageUrl', 'is_subscribed')
        depth = 1

class HuntTrainerSerializer(serializers.ModelSerializer):
    user = EmbedUserSerializer(many=False)
    
    class Meta:
        model = Trainer
        fields = ('id', 'bio', 'user')
        
class FollowerSerializer(serializers.ModelSerializer):
    trainer = EmbedTrainerSerializer(many=False)
    follower = EmbedTrainerSerializer(many = False)

    
    class Meta:
        model = Following
        fields = ('trainer', 'follower', 'created_on')

