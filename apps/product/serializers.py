from rest_framework import serializers
from apps.product.models import Category, Product


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryProductSerializer(read_only=True, many=False)
    class Meta:
        model = Product
        fields = '__all__'
