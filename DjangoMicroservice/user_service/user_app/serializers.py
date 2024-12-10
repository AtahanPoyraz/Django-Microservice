from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import re
from .models import UserModel

def validate_password(value):
    if len(value) < 8:
        raise serializers.ValidationError("Password must be at least 8 characters long.")
    
    if not any(char.islower() for char in value):
        raise serializers.ValidationError("Password must contain at least one lowercase letter.")
    
    if not any(char.isupper() for char in value):
        raise serializers.ValidationError("Password must contain at least one uppercase letter.")
    
    if not any(char.isdigit() for char in value):
        raise serializers.ValidationError("Password must contain at least one digit.")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise serializers.ValidationError("Password must contain at least one special character (!@#$%^&*()).")
    
    return value

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, value):
        raise serializers.ValidationError("Invalid email format.")
    
    return value

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


class CreateUserDTO(serializers.ModelSerializer):
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


class UpdateUserDTO(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser']

    def validate_email(self, value):
        return validate_email(value)

    def validate_password(self, value):
        if value:
            return validate_password(value)
        
        return value
