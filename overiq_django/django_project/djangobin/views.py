import datetime
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1> Working very Well </h1>")


def today_is(request):
    now = datetime.datetime.now()
    html = f"<html><body> Current date and time {now} </body></html>"
    return HttpResponse(html)


def profile(request):
    return HttpResponse("<p> Profile page of user </p>")


