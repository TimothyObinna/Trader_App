from django.urls import path
from .views import CategoryView, ProductView, ProductimageView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='cat_list'),
    path('products/', ProductView.as_view(), name='pro_list'),
    path('productimages/', ProductimageView.as_view(), name='proimage_list'),
]