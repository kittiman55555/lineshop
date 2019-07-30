from django.db import models
from categories.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    code = models.CharField(max_length=50)
    description = models.TextField()
    qty = models.IntegerField()
    weight = models.IntegerField()
    photo_main = models.ImageField(upload_to='product/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True)
    categories = models.ManyToManyField(Category)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.name
        




