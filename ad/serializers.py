## serilizers 
from rest_framework import serializers
from .models import Ad , Brand , Category , AdImages


class AdSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdImagesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = AdImages
        fields = '__all__'


class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'