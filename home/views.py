from django.shortcuts import render
from ad.models import Category
# Create your views here.
def home(request):
    all_category = Category.objects.filter(main_category=True)
    return render(request,'home/home.html',{'all_category':all_category})