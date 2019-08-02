from django.db import models
from product.models import Product
from datetime import datetime    

# Create your models here.
class Order(models.Model):
    status = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    address = models.TextField(blank=True)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    provice = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    weight = models.IntegerField()
    increment_id = models.IntegerField()
    subtotal = models.FloatField()
    shipping_method_name = models.CharField(max_length=50,blank=True)
    shipping_amount = models.FloatField()
    payment_method_name = models.CharField(max_length=50,blank=True)
    grand_total = models.FloatField()
    qty = models.IntegerField()
    productName = models.CharField(max_length=50)
    finalPrice = models.FloatField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE) 

    def __str__(self):
        return self.increment_id


    







