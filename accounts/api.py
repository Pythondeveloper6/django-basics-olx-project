from .models import Profile
from django.contrib.auth.models import User
from .serializers import UserSerializer , ProfileSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404




class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        profile = get_object_or_404(Profile,id=self.kwargs['pk'])
        print(profile)
        return profile



class ProfileEditView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 



