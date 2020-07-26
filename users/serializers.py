from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', )


class UserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
            'password2': self.validated_data.get('password2', ''),
        }
