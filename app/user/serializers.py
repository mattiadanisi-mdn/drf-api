from rest_framework import serializers
from user.models import User
from django.contrib.auth.models import User as BaseUser

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(many=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        base_user_data = validated_data.pop('user')
        base_user = BaseUserSerializer.create(BaseUserSerializer(), base_user_data)
        user = User.objects.create(user=base_user)
        return user