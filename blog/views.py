from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    all_posts = Post.objects.all()
    return render(request,'blog/all_posts.html' ,{'posts':all_posts})



def post_detail(request , id): # post 
    pass