from django.core.exceptions import RequestDataTooBig
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from Users.models import Topic, UserProfile, Thread, ThreadPosts

class AccountSerializer(serializers.ModelSerializer):
    class ProfileSerailizer(serializers.ModelSerializer):
        class Meta:
            model = UserProfile
            fields = []

    profile = ProfileSerailizer(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'profile']

    @staticmethod
    def create(validated_data):
        user_instance = User.objects.create_user(**validated_data)
        if 'profile' in validated_data.keys():
            profile_data = validated_data.pop('profile')
            UserProfile.objects.create(userID=user_instance, **profile_data)
        else:
            UserProfile.objects.create(userID=user_instance)
        return user_instance

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('__all__')

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadPosts
        fields = ('__all__')