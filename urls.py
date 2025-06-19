from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product-details/', views.product_details, name='product_details'),
    path('contact/', views.contact, name='contact'),
]

