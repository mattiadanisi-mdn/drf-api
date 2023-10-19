from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet

from adoption.serializers import AdoptionSerializer
from adoption.models import Adoption 

class AdoptionViewSet(ModelViewSet):
    serializer_class = AdoptionSerializer
    queryset = Adoption.objects.all()
    permission_classes = [permissions.IsAuthenticated]
        
    
        
        