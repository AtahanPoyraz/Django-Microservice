from rest_framework import serializers

class SendEmailSerializer(serializers.Serializer):
    to = serializers.EmailField(required=True)
    subject = serializers.CharField(max_length=255, required=True)
