from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about_us, name='about_us'),
    path('all_products/', product, name='all_products'),
    path('product_detail/<int:id>/', single_product, name='product_detail'),
    path('contact/', contact, name='contact'),
]