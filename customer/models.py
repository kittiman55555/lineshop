from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    name_line = models.CharField(max_length=50, blank=True)
    store_id = models.IntegerField(default=0, blank=True)
    line_id = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name