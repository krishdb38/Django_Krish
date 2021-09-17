
from django.urls import path, include
from django.shortcuts import HttpResponse

# Import Views Functions
from . import views

# Create Function
urlpatterns = [
    path('', views.index, name="index"),
    path('time/', views.today_is, name="time")
]
