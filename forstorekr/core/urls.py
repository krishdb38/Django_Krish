from django.urls import  path

from . views import (
    #ItemDetailView,
    
    )

app_name = "core" 

urlpatterns = [
    path('', HomeView.as_view(), name = "home")
]