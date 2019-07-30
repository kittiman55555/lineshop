from django.contrib import admin

# Register your models here.

from .models import Category


class CategoryAdmin(admin.ModelAdmin):  
        list_display = ('name',)
        #$list_display_link = ('id', 'name')
        #search_fields = ('name', 'email', 'listing')
        list_per_page = 25

admin.site.register(Category, CategoryAdmin)