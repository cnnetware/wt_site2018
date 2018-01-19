from django.db import models

# Create your models here.

class BlogsPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    createdate = models.DateTimeField()
    createuser = models.CharField(max_length=20)
