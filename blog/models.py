from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Foreign Key: user to post(one to many relationship)
    # on_delete: what happens to the post when the user is deleted?
    #       delete the post? set the author to none?
    #       CASCADE -> delete the post

    def __str__(self):
        return self.title
    # what will be printed out
