from rest_framework import viewsets
from blog.users.models import Blogger
from blog.posts.models import Post
from blog.posts.serializers import PostSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_pk")
        authors = Blogger.objects.get(user_id=user_id).follow.all()
        return self.queryset.filter(author__in=authors).order_by("-created_at")


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_pk")
        return self.queryset.filter(author_id=user_id).order_by("-created_at")

