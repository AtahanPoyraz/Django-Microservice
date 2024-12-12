import re
from rest_framework import serializers

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