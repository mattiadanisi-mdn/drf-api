from rest_framework.serializers import ModelSerializer, SlugRelatedField

from adoption.models import Adoption
from user.serializers import UserSerializer
from animal.serializers import AnimalSerializer

class AdoptionSerializer(ModelSerializer):
    owner = UserSerializer(many=False)
    animal = AnimalSerializer(many=False)

    class Meta:
        model = Adoption
        fields = '__all__'