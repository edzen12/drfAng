from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.product.models import Category, Product
from apps.product.serializers import CategoryProductSerializer, ProductSmallSerializer, ProductSerializer


class GetListAllCategoryProduct(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return Category.objects.all()
    

class GetListAllProduct(generics.ListAPIView):
    serializer_class = ProductSmallSerializer

    def get_queryset(self):
        return Product.objects.all()


class CreateCategory(APIView):
    """Создание Категории"""
    def post(self, request, format=None):
        serializer = CategoryProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('rest', status=status.HTTP_400_BAD_REQUEST)


class CreateProduct(APIView):
    """Создание Товара"""
    def post(self, request, format=None):
        serializer = ProductSmallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('rest', status=status.HTTP_400_BAD_REQUEST)