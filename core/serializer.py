from django.contrib.auth.models import User
from rest_framework import serializers

from shop.models import OrderDetail, Order
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(), source='category')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category','category_id', 'brand', 'image')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategoryAndProductSerializer(serializers.ModelSerializer):
    detail = ProductSerializer(many=True, read_only=True,)

    class Meta:
        model = Category
        fields = ('id', 'name', 'detail','product')
        depth = 1

