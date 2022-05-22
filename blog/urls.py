from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers

from blog.users.views import BloggerViewSet
from blog.posts.views import NewsViewSet, PostsViewSet

router = routers.SimpleRouter()
router.register(r"users", BloggerViewSet)
news_router = routers.NestedSimpleRouter(router, r"users", lookup="user")
posts_router = routers.NestedSimpleRouter(router, r"users", lookup="user")

news_router.register(r"news", NewsViewSet, basename="user-news")
posts_router.register(r"posts", PostsViewSet, basename="user-posts")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(news_router.urls)),
    path("api/v1/", include(posts_router.urls)),
]
