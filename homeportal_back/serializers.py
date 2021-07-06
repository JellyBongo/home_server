from rest_framework import serializers

from .models import Invitation, User

# General TODO:
# Create serializers. Learn how to pass images


class UserSerializer(serializers.ModelSerializer):
    # avatar = serializers.ImageField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'birthday', 'avatar_uuid']


class InvitationSerializer(serializers.ModelSerializer):
    # avatar = serializers.ImageField()
    class Meta:
        model = Invitation
        fields = ['token', 'expiration_date']
