from django.contrib.auth import authenticate
from rest_framework import serializers
from ..models import phone_regex


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, validators=[phone_regex])
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        attrs['user'] = user
        return attrs
