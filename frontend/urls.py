# frontend/urls.py or your app urls.py
from django.urls import path
from . import views

app_name = 'frontend'  # if you are using namespacing

urlpatterns = [
    path('add-stock/', views.add_stock, name='add_stock'),
]
