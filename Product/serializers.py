from unicodedata import category
from urllib import request
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
            image_url=validated_data['image_url'],
            category=validated_data['category']
        )
        product.save()
        return product

    def delete(self, instance):
        instance.delete()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.category = validated_data.get('category', instance.category)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        category = Category(
            name = validated_data['name'],
            description = validated_data['description']
        )
        category.save()
        return category

    def delete(self, instance):
        instance.delete()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance