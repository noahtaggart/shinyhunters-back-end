from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from app_api.models import Hunt, Following, Trainer
from app_api.serializers import HuntSerializer
from app_api.serializers.trainer_serializers import EmbedTrainerSerializer, FollowerSerializer

class TrainerView(ViewSet):
    
    def list(self, request):
        
        search_name = self.request.query_params.get("search_name", None)
        
        if search_name != None:
            trainers = Trainer.objects.filter(user__username__contains = search_name)
        else:
            trainers = Trainer.objects.all()
        
        for trainer in trainers:
            trainer.is_subscribed = request.auth.user
            
        
        serializer = EmbedTrainerSerializer(trainers, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        
        trainer = Trainer.objects.get(pk=pk)
        serializer = EmbedTrainerSerializer(trainer, many=False)
        return Response(serializer.data)
    
    @action(methods=['post', 'delete'], detail=True)
    def subscribe(self, request, pk):
        """post/delete requests for subscribing and unsubscribing"""
        response_message = ""
        follower = Trainer.objects.get(pk=request.auth.user.id)
        trainer = Trainer.objects.get(pk=pk)
        if request.method == 'POST':
            newSub = Following.objects.create(follower = follower, trainer = trainer)
            newSub.save()
            serializer = FollowerSerializer(newSub, context={'request': request})
            response_message = Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            sub = Following.objects.get(trainer=pk, follower_id=request.auth.user.id)
            sub.delete()
            response_message = Response(None, status=status.HTTP_204_NO_CONTENT)
        return response_message