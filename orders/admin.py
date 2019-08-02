from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):  
    list_display = ('created_at', 'updated_at', 'address')
    list_per_page = 25

admin.site.register(Order, OrderAdmin)