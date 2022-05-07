from django.urls import  path
from .views import dashboard

app_name = 'dwitter' # to remember which app urls 
urlpatterns = [
    path('', dashboard, name = "dashboard"),
]