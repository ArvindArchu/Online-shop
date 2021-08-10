from Shop.models import Product
from django.http import HttpResponse
from django.shortcuts import redirect, render
from.models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm 
from django.contrib.auth import login, authenticate 

#Home page view
def home(request):
	products = Product.objects.all()
	return render(request, 'Shop/shop.html',{'products':products})

#About page view
def about(request):
	return render(request, 'Shop/about.html')

#Create-product view
def product_create(request):
	if request.method == 'POST':
		form = productForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			# Get the current instance object to display in the template
			img_obj = form.instance
			return render(request, 'Shop/createProduct.html', {'form': form, 'img_obj': img_obj})
	else:
		form = productForm()

	return render(request, 'Shop/createProduct.html', {'form': form})
