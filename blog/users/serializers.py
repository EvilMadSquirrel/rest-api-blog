from blog.users.models import Blogger
from rest_framework import serializers


class BloggerSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True)
    readed_posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blogger
        fields = ["id", "posts", "follow", "readed_posts"]
