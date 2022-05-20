from rest_framework import serializers
from blog.posts.models import Post
from blog.users.serializers import UserSubscriberSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSubscriberSerializer(many=False)
    readers = UserSubscriberSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'readers']