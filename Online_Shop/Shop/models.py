from django.db import models
from django.contrib.auth.models import User

#Database for the products
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=200,default='Enter product name')
    price = models.DecimalField(max_digits=5, decimal_places=2,default='0.0')
    description = models.TextField(default='Enter product description')
    image = models.ImageField(upload_to='images/',null=True, blank=True, default='default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.productname


    