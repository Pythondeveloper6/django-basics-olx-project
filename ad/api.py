### like view  : api view
from .models import Ad
from .serializers import AdSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_ad_list(request):
    ads = Ad.objects.all()
    data = AdSerilizer(ads , many=True).data
    return Response({'data':data})