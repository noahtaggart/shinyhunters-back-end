from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from app_api.models.method import Method

from app_api.serializers.method_serializer import EmbedMethodSerializer



class MethodView(ViewSet):
    
    def list(self, request):
        method = Method.objects.all()
        
        serializer = EmbedMethodSerializer(method, many=True)
        return Response(serializer.data)