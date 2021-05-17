from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.TextField(default='')

class UserProfile(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    # topicID = models.ForeignKey(Topic, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return "user_" + str(self.pk) + "_" + str(self.userID.username)

class Thread(models.Model):
    content = models.TextField(default='')
    media = models.FileField(upload_to=None,max_length=256)
    userID=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    createdAt =  models.DateTimeField(auto_now_add=True)
    topicID= models.ForeignKey(Topic,on_delete=models.PROTECT)

class ThreadPosts(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(default="")
    threadID = models.ForeignKey(Thread, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)