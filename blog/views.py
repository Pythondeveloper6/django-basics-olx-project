from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    all_posts = Post.objects.filter(active=True)
    return render(request,'blog/all_posts.html' ,{'posts':all_posts})



def post_detail(request , slug): # post 
    post_detail = Post.objects.get(post_slug=slug)
    return render(request,'blog/post_detail.html',{'post':post_detail})