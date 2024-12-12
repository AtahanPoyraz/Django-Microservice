from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import re
from .models import UserModel
from .validators import *

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  
        }

    def validate_password(self, value):
        return validate_password(value)

    def validate_email(self, value):
        return validate_email(value)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser']

    def validate_password(self, value):
        return validate_password(value)

    def validate_email(self, value):
        return validate_email(value)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser']

    def validate_email(self, value):
        return validate_email(value)

    def validate_password(self, value):
        if value:
            return validate_password(value)
        
        return value
