from django.urls import path
from app1 import views

app_name='app1'

urlpatterns = [
    path('',views.app1,name='app1'),
    path('customers',views.customers,name='customer'),
    path('products',views.products,name='products'),
    path('orders',views.orders,name='orders'),
]