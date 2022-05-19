from django.db import models
from django.contrib.auth.models import User


class UserSubscriber(models.Model):
    user = models.ForeignKey(User, related_name='subscribed', on_delete=models.PROTECT, null=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers')


