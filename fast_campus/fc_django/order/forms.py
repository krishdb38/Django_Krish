from django import forms
from django.http import request
from product.forms import RegisterForm
from fcuser.models import Fcuser
from product.models import Product
from .models import Order

from django.db import transaction

class RegisterForm(forms.Form):
    def __init__(self,request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
    
    quantity = forms.IntegerField(
        error_messages= {"required":"Input quantity"},
        label= "Quantity"
        )
    product = forms.IntegerField(error_messages={
        "required" : "Select Product "
        }, label="Product Detail", widget= forms.HiddenInput)


    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        product = cleaned_data.get("product")
        fcuser = self.request.session.get("user")
        
        if quantity and product and fcuser :
            with transaction.atomic():
                prod = Product.objects.get(pk = Product)
                order = Order (
                    quantity= quantity,
                    product = product, 
                    fcuser = Fcuser.objects.get(email = fcuser)
                )
                order.save()
                prod.stock -= quantity
        else:
            self.add_error("product", "no value")
            self.add_error("quantity", "no value")
            #self.add_error("product", "No Value ")