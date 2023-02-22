from django.db import models
from django.contrib.auth.models import User
import datetime

class Post(models.Model):
    title = models.CharField(max_length = 500)
    post_image = models.ImageField(upload_to = 'post', blank = True)
    summary = models.TextField(max_length = 5000)
    content = models.TextField(max_length = 10000)
    publication_date = models.DateTimeField(default = datetime.datetime.now())
    author = models.CharField(max_length = 250)
    total_likes = models.IntegerField()
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    liked_date = models.DateTimeField(default = datetime.datetime.now())