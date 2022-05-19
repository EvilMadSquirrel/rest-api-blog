from django.db import models
from django.contrib.auth.models import AbstractUser, User

from blog.posts.models import Post


class UserSubscriber(AbstractUser):
    user = models.ForeignKey(User, related_name='subscribed', on_delete=models.PROTECT, null=True)
    subscribers = models.ForeignKey(User, related_name='subscribers', on_delete=models.PROTECT, null=True)
    readed_posts = models.ForeignKey(Post, related_name='readed_posts', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.get_full_name()
