import imp
from django.http import HttpResponse
from invoices.models import Invoice
from django.shortcuts import render



def hello_word(request):
    obj = Invoice.objects.get(id=1)
    qs = Invoice.objects.all()
    print(obj.__dict__)

    print('***')
    print(qs.query)
    return render(request, 'home.html', )
    #return render(request, '')
