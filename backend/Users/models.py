from django.db import models
from django.contrib.auth.models import User

# Create your models here.



def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Topic(models.Model):
    name = models.TextField(default='')

class UserProfile(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    # topicID = models.ForeignKey(Topic, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return "user_" + str(self.pk) + "_" + str(self.userID.username)

class Thread(models.Model):
    title = models.TextField(default='')
    content = models.TextField(default='')
    media = models.FileField(upload_to=upload_to,max_length=256, blank=True, default='posts/default.jpg')
    userID=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    createdAt =  models.DateTimeField(auto_now_add=True)
    topicID= models.ForeignKey(Topic,on_delete=models.PROTECT)

class ThreadPosts(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(default="")
    threadID = models.ForeignKey(Thread, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)