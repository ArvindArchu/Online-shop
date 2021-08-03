from Shop.models import Product
from django.shortcuts import render
from.models import*

def home(request):
	products = Product.objects.all()
	return render(request, 'Shop/shop.html',{'products':products})

