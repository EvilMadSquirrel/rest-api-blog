from rest_framework import viewsets
from blog.posts.models import Post
from blog.posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

