from django.urls import path
from apps.product.views import GetListAllCategoryProduct, GetListAllProduct, CreateCategory, CreateProduct


urlpatterns = [
    path('list/all/category/product/', GetListAllCategoryProduct.as_view()),
    path('list/all/product/', GetListAllProduct.as_view()),
    path('create/category/', CreateCategory.as_view()),
    path('create/product/', CreateProduct.as_view()),
]

