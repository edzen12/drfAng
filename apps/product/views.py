from rest_framework import generics
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
    def post(self, request, format=None):
        print("rest")
        return Response('rest', status=status.HTTP_201_CREATED)