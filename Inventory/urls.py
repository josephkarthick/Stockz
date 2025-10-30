from django.urls import path
from . import views

app_name = 'Inventory'

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/category/', views.category, name='category'),
    path('products/sub-category/', views.sub_category, name='sub_category'),
    path('products/brands/', views.brands, name='brands'),
    path('products/units/', views.units, name='units'),
    path('products/sku/', views.sku, name='sku'),    
]