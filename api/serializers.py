
# Auto generated by Django helper
from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = CustomUser
