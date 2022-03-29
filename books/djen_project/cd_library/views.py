from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def hello_world(request,):
    context = {"username" : "Krishna"}
    return render(request, 'hello_word.html', context)