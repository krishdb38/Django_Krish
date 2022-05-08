import imp
from re import template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView
from .models import Invoice
from profiles.models import Profile
from .forms import InvoiceForm
from django.urls import reverse_lazy
# Create your views here.

class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/main.html" # invoice list 
    #paginate_by 
    context_object_name = "qs" # over riding default

    def get_queryset(self) :
        #profile = Profile.objects.get(user = self.request.user)
        profile = get_object_or_404(Profile, user = self.request.user)
        qs = Invoice.objects.filter(profile).order_by('-created')
        return qs
        # 3.04.10

class InvoiceFormView(FormView):
    form_class = InvoiceForm
    template_name = "invoices/create.html"

    success_url = reverse_lazy('invoices:main')

    def form_valid(self, form):
        profile = Profile.objects.get(user = self.request.user)
        instance = form.save(commit = False)
        instance.profile = profile
        form.save()

        return super().form_valid(form)