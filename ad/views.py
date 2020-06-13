from django.shortcuts import render
from .forms import AdForm
# Create your views here.




def all_ads(request):
    pass

def all_categories(request):
    pass

def category_ads(request , id):
    pass



def add_ad(request):
    
    return render(request,'ad/add_ad.html',{})
