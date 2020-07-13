## serilizers 
from rest_framework import serializers
from .models import Ad


class AdSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'