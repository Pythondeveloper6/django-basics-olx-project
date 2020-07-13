### like view  : api view
from .models import Ad
from .serializers import AdSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


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


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerilizer