"""View module for handling requests about game types"""
import uuid
import base64
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Photo, Trainer
from django.core.files.base import ContentFile


class PhotoView(ViewSet):
    """Rater app Photo view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Photo
        
        Returns:
            Response -- JSON serialized Photo
        """
        
        try:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        except Photo.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all photos
        
        Returns:
            Response -- JSON serialized list of photos
        """
        photos = Photo.objects.all()
        
        
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        
        Returns
            Response -- JSON serialized photo instance
        """
        trainer = Trainer.objects.get(user=request.auth.user)
        format, imgstr = request.data["trainer_image"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["trainer_id"]}-{uuid.uuid4()}.{ext}')
    
        photo = Photo.objects.create(
            photo= data,
            trainer = trainer
        )
        
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)
    

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for photos"""
    class Meta:
        model = Photo
        fields = ('id', 'photo', 'trainer')
        depth = 2