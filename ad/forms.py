from django import forms
from .models import Ad




class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['code','owner','name','image','content','price','category']
