from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from app_api.models import Hunt, Following
from app_api.serializers import HuntSerializer




class HuntView(ViewSet):
    
    def list(self, request):
        hunts = Hunt.objects.filter(completed=True)
        
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def subscriptions(self, request):
        followerId=request.auth.user.id
        subscriptions = Following.objects.filter(follower_id = followerId)
        
        subscribed_hunts = []
        
        for subscription in subscriptions:
            hunts = Hunt.objects.filter(trainer=subscription.trainer).filter(completed=True)
            subscribed_hunts.append(hunts)
            
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)
        
        
    
    
    
    
        