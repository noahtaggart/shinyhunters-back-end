from app_api.serializers.trainer_serializers import EmbedUserSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class UserView(ViewSet):
    
    def list(self, request):
        user = request.auth.user
        
        serializer = EmbedUserSerializer(user)
        return Response(serializer.data)