from django.db import models
from blog.users.models import UserSubscriber


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserSubscriber, related_name='posts', on_delete=models.CASCADE, null=False)
    readers = models.ManyToManyField(UserSubscriber, related_name='readed_posts')

    def __str__(self):
        return self.title
