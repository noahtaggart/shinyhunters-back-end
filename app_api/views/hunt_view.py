from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action
from app_api.models import Hunt
from app_api.serializers import HuntSerializer




class HuntView(ViewSet):
    
    def list(self, request):
        hunts = Hunt.objects.all()
        
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)
    
    
    
    
        