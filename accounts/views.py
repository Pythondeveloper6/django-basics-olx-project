from django.shortcuts import render
from .forms import UserForm
from .models import Profile
from django.contrib.auth import authenticate
# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

    else:
        form = UserForm()

    return render(request,'registeration/signup.html',{'form':form})