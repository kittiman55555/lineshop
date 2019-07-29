from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name_line = models.CharField(max_length=50)
    store_id = models.IntegerField(default=0, blank=True)
    line_id = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.first_name