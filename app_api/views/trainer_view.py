from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from app_api.models import Hunt, Following, Trainer
from app_api.serializers import HuntSerializer
from app_api.serializers.trainer_serializers import EmbedTrainerSerializer

class TrainerView(ViewSet):
    
    def list(self, request):
        trainers = Trainer.objects.all()
        
        serializer = EmbedTrainerSerializer(trainers, many=True)
        return Response(serializer.data)