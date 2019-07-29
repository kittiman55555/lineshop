from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):  
        list_display = ('name', 'price')
        #$list_display_link = ('id', 'name')
        search_fields = ('name', 'price')
        list_per_page = 25

admin.site.register(Product, ProductAdmin)
