from django.db import models
from blog.users.models import Blogger


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Blogger, related_name="posts", on_delete=models.CASCADE, null=False
    )
    readers = models.ManyToManyField(Blogger, related_name="readed_posts")
