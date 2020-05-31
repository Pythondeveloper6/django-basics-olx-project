from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


    # post : 
    #     - title
    #     - author # relation
    #     - createed_at
    #     - content

class Post(models.Model): # db table
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    created_at =models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

