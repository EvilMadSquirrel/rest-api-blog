from mixer.backend.django import mixer
from blog.users.models import Blogger
from blog.posts.models import Post


def create_users():
    users = mixer.cycle(3).blend(Blogger, password='111')
    return users


def fill_blogs():
    users = Blogger.objects.all()

    for user in users:
        posts = mixer.cycle(5).blend(Post, author=user)
        print(posts)
