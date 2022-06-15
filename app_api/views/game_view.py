from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from app_api.models.game import Game

from app_api.serializers.game_serializer import EmbedGameSerializer



class GameView(ViewSet):
    
    def list(self, request):
        game = Game.objects.filter(id__gte=23).order_by('-id')
        
        serializer = EmbedGameSerializer(game, many=True)
        return Response(serializer.data)