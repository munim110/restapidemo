from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product(
            name=validated_data['name'],
            price=validated_data['price'],
            stock=validated_data['stock'],
            image_url=validated_data['image_url']
        )
        product.save()
        return product