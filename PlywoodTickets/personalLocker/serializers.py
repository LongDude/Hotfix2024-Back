from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['firstname','surname','patronymic','phonenumber', 'email', 'gender', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            surname=validated_data['surname'],
            patronymic=validated_data.get('patronymic', None),
            phonenumber=validated_data['phonenumber'],
            gender=validated_data['gender'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserHistorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['path', 'title']
