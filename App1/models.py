from django.db import models
from django.contrib.auth.models import User
import datetime

class Post(models.Model):
    title = models.CharField(max_length=500)
    summary = models.TextField(max_length=5000)
    content = models.TextField(max_length=10000)
    publication_date = models.DateTimeField(default=datetime.datetime.now())
    author = models.CharField(max_length=250)
    total_likes = models.IntegerField()
    # like = models.BooleanField(default=False)
    # user_like = models.ForeignKey(User, )