from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from blog.users.views import UserViewSet
from blog.posts.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
