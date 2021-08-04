from django.urls import path
from . import views #importing views.py file from local directory

urlpatterns = [
    path('home/', views.home, name = 'shop-home'),#giving no path and then importing home from views
    path('about/',views.about,name = 'shop-about'),
]