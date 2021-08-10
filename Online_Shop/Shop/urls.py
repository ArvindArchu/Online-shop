from django.urls import path
from .import views #importing views.py file from local directory
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib import admin


#Projet urls
urlpatterns = [
    path('home/', views.home, name = 'shop-home'),
    path('about/',views.about,name = 'shop-about'),
    path('create/',views.product_create,name = 'shop-create'),
]
