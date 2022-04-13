from dataclasses import fields
from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['discord_id', 'avatar', 'email',  'name', 'wordle', 'papertoss', 'points_spent']
    