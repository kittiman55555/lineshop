from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    name_line = models.CharField(max_length=50, blank=True)
    store_id = models.IntegerField(default=0, blank=True)
    line_id = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    district = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50,blank=True)
    provice = models.CharField(max_length=50,blank=True)
    country = models.CharField(max_length=50,default='Thailand')
    zipcode = models.CharField(max_length=10,blank=True)
    email = models.CharField( max_length=50,blank=True)
    store_id = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.first_name