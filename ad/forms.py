from django import forms
from .models import Ad , Comment




class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['name','image','content','price','category']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
