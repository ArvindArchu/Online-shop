from django.urls import path
from .import views #importing views.py file from local directory
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib import admin


#Projet urls
app_name = 'Shop'
urlpatterns = [
    path('', views.home, name='shop-home'),
    path('home/', views.home, name = 'shop-home'),
    path('about/',views.about,name = 'shop-about'),
    path('create/',views.product_create,name = 'shop-create'),
    path('edit/<int:myid>/',views.product_edit,name = 'shop-edit'),
    path('product/<int:myid>/',views.product,name = 'shop-productInfo'),
    path('checkout/<int:myid>/',views.checkout,name = 'shop-checkout'),
]
