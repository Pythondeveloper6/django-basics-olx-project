from django.db import models

# Create your models here.


    # post : 
    #     - title
    #     - author
    #     - createed_at
    #     - content

class Post(models.Model): # db table
    title = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100 , default='')
    email = models.EmailField()
    content = models.TextField(max_length=1000)


    

