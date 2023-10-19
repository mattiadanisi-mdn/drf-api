from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Animal.objects.all()
    