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
            for hunt in hunts:
                subscribed_hunts.append(hunt)
            
        serializer = HuntSerializer(subscribed_hunts, many=True)
        return Response(serializer.data)
