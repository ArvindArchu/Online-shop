from Shop.models import Product
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


#Home page view
def home(request):
	products = Product.objects.all()
	return render(request, 'Shop/shop.html',{'products':products})

#About page view
def about(request):
	return render(request, 'Shop/about.html')

#Checkout view
def checkout(request,myid):
	if request.method == 'POST':
		form = checkoutForm(request.POST)
		if form.is_valid():
			product = Product.objects.get(productID = myid)
			product.stock -= 1
			product.save(update_fields=['stock'])
			return redirect("Shop:shop-home")
	else:
		form = checkoutForm()
		
	return render(request, 'Shop/checkout.html', {'form': form})
	
	
#Create-product view
def product_create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = productForm(request.POST, request.FILES)
			if form.is_valid():
				prod = form.save(commit=False)
				prod.author = request.user
				prod.save()
				# Get the current instance object to display in the template
				img_obj = form.instance
				return redirect("Shop:shop-home")
				return render(request, 'Shop/createProduct.html', {'form': form, 'img_obj': img_obj})
		else:
			form = productForm()
	else:
		messages.error(request, "You must be logged in to sell a product.")
		return redirect("users:login")

	return render(request, 'Shop/createProduct.html', {'form': form})

def product_edit(request, myid):
	product = Product.objects.get(productID = myid)
	form = productForm(request.POST, request.FILES, instance=product)
	if form.is_valid():
		prod = form.save(commit=False)
		prod.author = request.user
		prod.save()
		return redirect("Shop:shop-home")
	
	return render(request, 'Shop/createProduct.html', {'form': form})
	

#Product-page view
def product(request, myid):
	product = Product.objects.get(productID = myid)
	return render(request, 'Shop/productInfo.html', {'product': product})
