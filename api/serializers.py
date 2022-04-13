from dataclasses import fields
from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['discord_id', 'avatar', 'email', 'name', 'wordle', 'papertoss', 'points_spent']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['discord_id', 'avatar', 'email', 'name', 'wordle', 'papertoss', 'points_spent']

    def create(self, validated_data):
        """
        Create and return a new `Data` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Data` instance, given the validated data.
        """
        instance.discord_id = validated_data.get('discord_id', instance.discord_id)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.wordle = validated_data.get('wordle', instance.wordle)
        instance.papertoss = validated_data.get('papertoss', instance.papertoss)
        instance.points_spent = validated_data.get('points_spent', instance.points_spent)
        instance.save()
        return instance


class HighscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['discord_id', 'avatar', 'email', 'name', 'wordle', 'papertoss', 'points_spent']

    def create(self, validated_data):
        """
        Create and return a new `Data` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Data` instance, given the validated data.
        """
        instance.discord_id = validated_data.get('discord_id', instance.discord_id)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.wordle = validated_data.get('wordle', instance.wordle)
        instance.papertoss = validated_data.get('papertoss', instance.papertoss)
        instance.points_spent = validated_data.get('points_spent', instance.points_spent)
        instance.save()
        return instance
