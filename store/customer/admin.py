from django.contrib import admin

# Register your models here.

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):  
        list_display = ('first_name', 'last_name')
        #$list_display_link = ('id', 'name')
        #search_fields = ('name', 'email', 'listing')
        list_per_page = 25

admin.site.register(Customer, CustomerAdmin)