from rest_framework import serializers
from animal.models import Animal
from user.serializers import UserSerializer

class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'