from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('firstpage', views.firstpage, name='firstpage'),
    path('logout', views.logout, name='logout'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('index', views.index, name='index'),
    path('adminregister', views.adminregister, name='adminregister'),
    path('productitems', views.product_items, name='product_items'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('allproduct', views.allproduct, name='allproduct'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)