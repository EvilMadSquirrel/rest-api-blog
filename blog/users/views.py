from rest_framework import viewsets
from blog.users.models import UserSubscriber
from blog.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserSubscriber.objects.all().order_by('-user__date_joined')
    serializer_class = UserSerializer
