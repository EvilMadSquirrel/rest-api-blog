from rest_framework import viewsets
from blog.users.models import Blogger
from blog.users.serializers import BloggerSerializer


class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
