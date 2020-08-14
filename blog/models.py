from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    #date_posted=models.DateTimeField(auto_now_add=True)#it means timestamp will be
    # updated when post is updated
    #for auto_now the post should be created  to update the timestamp
    data_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


