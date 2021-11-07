import django.http
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from product.models import Product
from order.forms import RegisterForm as OrderForm

# rest frame work view
from rest_framework import generics
from rest_framework import mixins

from product.serializers import ProductSerializer


from .forms import RegisterForm

# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "product_list"
    
class ProductCreate(FormView):    
    template_name = "register_product.html"
    form_class = RegisterForm
    success_url = "/product"
    
    
class ProductDetail(DetailView):
    "variable names must be same as Detail View other wise need to over ride "
    template_name = "product_detail.html"
    queryset = Product.objects.all() # if you want filter then apply filter here
    context_object_name = "product" # this is use to do for loop in template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["form"] = OrderForm(self.request)
        return context
    
class ProductListAPI(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all().order_by("id")
    
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        return self.retrieve (request, *args, **kwargs)
