from django.contrib.auth.models import User

from blog.users.models import UserSubscriber
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class UserSubscriberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    subscribers = UserSerializer(many=True, required=False)

    class Meta:
        model = UserSubscriber
        fields = ['user', 'subscribers']
