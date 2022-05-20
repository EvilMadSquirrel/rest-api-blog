from mixer.backend.django import mixer
from blog.users.models import UserSubscriber
from blog.posts.models import Post


def create_users():
    users = mixer.cycle(5).blend(UserSubscriber)
    return users


def create_posts():
    posts = mixer.cycle(10).blend(Post)
    return posts


def fill_blogs():
    users = UserSubscriber.objects.all()

    for user in users:
        posts = mixer.cycle(20).blend(Post, author=user)
        print(posts)
