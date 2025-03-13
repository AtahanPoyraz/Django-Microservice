from rest_framework import serializers
from .models import UserModel

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}} 

    def create(self, validated_data):
        password = validated_data.pop("password", None) 
        user = super().create(validated_data)  

        if password:  
            user.set_password(password)  
            user.save() 

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)  

        if password:
            instance.set_password(password)

        return super().update(instance, validated_data)
