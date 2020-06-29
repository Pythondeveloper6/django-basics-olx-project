from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phone_number']