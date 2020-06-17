from django import forms
from .models import Ad




class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['name','image','content','price','category']
