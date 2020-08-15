from django.shortcuts import get_object_or_404, render
from .forms import AdForm , CommentForm
from .models import Ad , Category , Comment
# Create your views here.




def all_ads(request):
    all_Ads = Ad.objects.all()
    print(all_Ads)
    return render(request,'ad/all-ads.html',{'ads':all_Ads})


# class Adlist(ListView , CreateView):
#     model = Ad
#     template_name = 'ad/all-ads.html'


def single_ad(request,id):
    ad = Ad.objects.get(id=id)
    comments = Comment.objects.filter(ad=ad)


    if request.method == 'POST': ## save
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.ad = ad
            myform.save()
    else:
        form = CommentForm()

    return render(request,'ad/single.html',{'ad':ad , 'comments' : comments , 'form':form})


def all_categories(request):
    all_category = Category.objects.filter(main_category=None)
    print(all_categories)
    return render(request,'ad/all-category.html',{'all_category':all_category})


def category_ads(request , id):
    category = get_object_or_404(Category,id=id)
    category_ads = Ad.objects.filter(category=category)

    return render(request,'ad/category_ads.html',{'category_ads':category_ads})



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



def like_ad(request,id):
    pass