from django.db import models
from django.contrib.auth.admin import User


# Create your models here.

class BbsUser(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=64, default='')
    head_img = models.ImageField(upload_to='upload/user/', default='upload/user/user01.img')

    def __unicode__(self):
        return self.user.username


class BbsPost(models.Model):
    author = models.ForeignKey(BbsUser)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

