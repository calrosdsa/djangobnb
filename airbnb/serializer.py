from django.contrib.postgres import fields
from .models import Ciudades,Cities,ProductImage
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=['image']

class CitiesSerializer(serializers.ModelSerializer):
    image=ProductImageSerializer(many=True)
    class Meta:
        model=Cities
        fields=['title','price','image','description','slug','detalles','ciudades']

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ciudades
        fields=['name','slug']