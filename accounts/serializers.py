from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile



class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = User
        fileds = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
