from django.urls import path
from . import views

urlpatterns=[
    path('',views.login),
    path('register',views.register),
    path('1',views.firstpage),
    path('logout',views.logout),
    path('adminlogin',views.adminlogin),
    path('index',views.index),
    path('adminregister',views.adminregister),
    path('products', views.product, name='product_list'),
    path('productitems', views.product_items),
    path('deleteproduct', views.delete_product),

]