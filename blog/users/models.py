from django.db import models
from django.contrib.auth.models import User


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow = models.ManyToManyField('self', related_name='followers', symmetrical=False)





