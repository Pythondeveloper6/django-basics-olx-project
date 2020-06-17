from django.shortcuts import render
from .forms import AdForm
from .models import Ad
# Create your views here.




def all_ads(request):
    all_Ads = Ad.objects.all()
    print(all_Ads)
    return render(request,'ad/all-ads.html',{'ads':all_Ads})


def all_categories(request):

    return render(request,'ad/all-category.html',{})


def category_ads(request , id):
    

    return render(request,'ad/caregory_ads.html',{})



def add_ad(request):
    if request.method == 'POST':  ## save
        form = AdForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
    else:
        form = AdForm()

    return render(request,'ad/post-ad.html',{'form':form})
