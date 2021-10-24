from django.contrib import admin
from order.models import Order
from . models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("fcuser", "product")
    
admin.site.register(Order, OrderAdmin)