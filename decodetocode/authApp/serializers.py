from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user data."""
    
    class Meta:
        model = User
        fields = ['cf_handle', 'email_id', 'first_name', 'last_name', 'rating']
 
class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    class Meta:
        model = User
        fields = ['cf_handle', 'email_id', 'first_name', 'last_name', 'rating', 'password']
    
    def create(self, validated_data):
        """Override create method to hash the password before saving."""
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    
    email_id = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        """Validate email and password."""
        try:
            user = User.objects.get(email_id=data['email_id'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Incorrect password.")
        
        return user
