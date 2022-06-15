from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from app_api.models import Hunt, Following, Trainer, Pokemon
from app_api.models.game import Game
from app_api.models.method import Method
from app_api.serializers import HuntSerializer
from rest_framework import status
from django.core.exceptions import ValidationError




class HuntView(ViewSet):
    
    def list(self, request):
        hunts = Hunt.objects.filter(completed=True).order_by('-date_completed')
        
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        hunt = Hunt.objects.get(pk=pk)
        
        serializer = HuntSerializer(hunt, many=False)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def subscriptions(self, request):
        followerId=request.auth.user.id
        subscriptions = Following.objects.filter(follower_id = followerId)
        
        subscribed_hunts = []
        
        for subscription in subscriptions:
            hunts = Hunt.objects.filter(trainer=subscription.trainer).filter(completed=True).order_by('-date_completed')
            for hunt in hunts:
                subscribed_hunts.append(hunt)
            
        serializer = HuntSerializer(subscribed_hunts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handles POST operations
        returns 
            Response -- JSON serialized hunt instance"""
        
        trainer = Trainer.objects.get(pk=request.auth.user.id)
        method = Method.objects.get(pk=request.data['method'])
        pokemon = Pokemon.objects.get(pk=request.data['pokemon'])
        game = Game.objects.get(pk=request.data['game'])
        
        hunt = Hunt.objects.create(
        trainer = trainer,
        encounters = 0,
        method = method,
        pokemon = pokemon,
        game = game,
        shiny_charm = request.data['shiny_charm'],
        date_started = datetime.now())
        
        try:
            serializer = HuntSerializer(hunt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)  
        
        
    @action(methods=['get'], detail=False)
    def all(self, request):
        hunts = Hunt.objects.all()
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)
            
            
    @action(methods=['get'], detail=False)
    def user_completed(self, request):
        hunts = Hunt.objects.filter(trainer=request.auth.user.id).filter(completed=True).order_by('-date_completed')
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def user_ongoing(self, request):
        hunts = Hunt.objects.filter(trainer=request.auth.user.id).filter(completed=False).order_by('-date_started')
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)
    
    @action(methods=['put'], detail=True)
    def add_encounter(self, request, pk):
        hunt = Hunt.objects.get(pk=pk)
        hunt.encounters = hunt.encounters + 1
        hunt.save()
        return Response({'message':'encounter added'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['put'], detail=True)
    def complete_hunt(self, request, pk):
        hunt = Hunt.objects.get(pk=pk)
        hunt.completed = True
        hunt.date_completed = datetime.now()
        hunt.save()
        return Response({'message':'hunt completed'}, status=status.HTTP_204_NO_CONTENT)