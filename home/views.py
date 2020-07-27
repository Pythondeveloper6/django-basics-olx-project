from django.shortcuts import render
from ad.models import Category , Ad
# Create your views here.
def home(request):
    all_category = Category.objects.filter(main_category=True)
    trending = Ad.objects.filter(trending=True)
    
    print(trending)

    return render(request,'home/home.html',{
        'all_category':all_category , 
        'trending_ads' : trending
        })