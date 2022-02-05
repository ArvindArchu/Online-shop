from django import forms
from django.forms import fields
from .models import *

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('author',)
        fields = ['productname','price','description','stock','image']

class checkoutForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField(max_length=12)