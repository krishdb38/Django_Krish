from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name = 'home'),
    path('index/', views.index, name = 'register'),
    path('emp', views.emp, name = 'emp')
]