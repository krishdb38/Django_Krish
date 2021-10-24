from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    
admin.site.register(Product, ProductAdmin)
# put model first and modelAdmin then