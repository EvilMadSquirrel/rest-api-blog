from mixer.backend.django import mixer
from blog.users.models import Blogger
from blog.posts.models import Post

BLOGGERS_COUNT = 3
POSTS_COUNT = 5


def create_users():
    users = mixer.cycle(BLOGGERS_COUNT).blend(Blogger, password='111')
    return users


def fill_blogs():
    users = Blogger.objects.all()

    for user in users:
        posts = mixer.cycle(POSTS_COUNT).blend(Post, author=user)
        print(posts)
