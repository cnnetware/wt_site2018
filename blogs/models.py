from django.db import models

# Create your models here.

class BlogsPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True)
    createuser = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-createdate']


