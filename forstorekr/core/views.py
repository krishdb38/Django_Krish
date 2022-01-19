from django.shortcuts import render
import  random
import  string

import  stripe
from django.conf import  settings
from django.contrib import  messages
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import  get_object_or_404
from django.utils import  timezone
from django.views.generic import  ListView, DetailView, View

from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import  Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def create_ref_code():
    "Create random mix number "
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k = 20))

def products(request):
    context = {'items': Item.objects.all()}
    return render(request, "products.html", context=context)

def is_valid_form(values):
    valid = True
    for field in values:
        if field == "":
            # when not valid
            valid = False
    return valid


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user = self.request.user, ordered = False)
            form = CheckoutForm()
            context = {
                "form":form,
                "couponform":CouponForm(),
                "order":order,
                "DISPLAY_COUPON_FORM":True
            }
            
            shipping_address_qs = Address.objects.filter(
                user = self.request.user,
                address_type = "S",
                default = True,
            )
            if shipping_address_qs.exists():
                context.update(
                    {"default_shipping_address" : shipping_address_qs[0]}
                )
            billing_address_qs = Address.objects.filter(
                user = self.request.user,
                address_type = "B",
                default = True
            )
            if billing_address_qs.exists():
                context.update(
                    {"default_billing_address": billing_address_qs[0]}
                )
            return render(self.request, "checkout.html", context=context)
