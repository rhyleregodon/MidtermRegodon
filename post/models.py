from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    date_created = models.DateTimeField('Date Created', default=datetime.now)
    date_updated = models.DateTimeField('Date Updated', default=datetime.now)
    content = models.TextField(max_length = 100)
    #is_active = False

    def __str__(self):
        return 'Post: {}'.format(self.title)


class Comment(models.Model):
    date_created =  models.DateTimeField('Date Created', default=datetime.now)
    content = models.TextField(max_length = 100)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')

    def __str__(self):
        return 'Comment: {}'.format(self.content)