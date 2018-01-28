from django.db import models

# Create your models here.

class MenuParam(models.Model):
    flag = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=40, null=False)
    status = models.IntegerField()

    def __unicode__(self):
        return self.title
