from django.db import models
from product.models import Product
from datetime import datetime    

# Create your models here.
class Order(models.Model):
    status = models.IntegerField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    address = models.TextField(blank=True)
    district = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50,blank=True)
    provice = models.CharField(max_length=50,blank=True)
    zipcode = models.CharField(max_length=10,blank=True)
    weight = models.IntegerField(blank=True)
    increment_id = models.IntegerField(blank=True)
    subtotal = models.FloatField(blank=True)
    shipping_method_name = models.CharField(max_length=50,blank=True)
    shipping_amount = models.FloatField(blank=True)
    payment_method_name = models.CharField(max_length=50,blank=True)
    grand_total = models.FloatField(blank=True)
    qty = models.IntegerField(blank=True)
    productName = models.CharField(max_length=50,blank=True)
    finalPrice = models.FloatField(blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE) 

    def __str__(self):
        return self.increment_id


    







