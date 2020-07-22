### like view  : api view
from .models import Ad , Category , Brand , AdImages
from .serializers import AdSerilizer , CategorySerilizer , BrandSerilizer , AdImagesSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import permissions


@api_view(['GET'])
def api_ad_list(request):
    ads = Ad.objects.all()
    data = AdSerilizer(ads , many=True).data
    return Response({'data':data})


@api_view(['GET','PUT'])
def api_ad_detail(request,id):
    ad = Ad.objects.get(id=id)
    data = AdSerilizer(ad).data
    return Response({'data':data})



class AdListView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerilizer
    permission_classes = [permissions.IsAuthenticated]


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerilizer
    permission_classes = [permissions.IsAuthenticated]




class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer
    permission_classes = [permissions.IsAuthenticated]


class CategoryAdsListView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = AdSerilizer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category = get_object_or_404(Category,id=self.kwargs['pk'])
        category_ads = Ad.objects.filter(category=category)
        return category_ads

    # def get_object(self):
    #     category = super().get_object()
    #     category_ads = Ad.objects.filter(category=category)
    #     return category_ads
    #          10   [2,3,4,5,6]
    # def sum(*args,**kwargs):
    #     pass

    # sum(10,2,3,4,5,6)


