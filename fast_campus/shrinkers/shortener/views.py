from django.shortcuts import render
from . models import Users

# Create your views here.
def index(request):
    user = Users.objects.filter(username = 'admin').first()
    email = user.email if user else 'Anonymous User'
    print(email)
    print(request.user.is_authenticated)

    if request.user.is_authenticated is False:
        email = "Anonymous User"
        print(email)
    return render(request, 'shortener/base.html', {'welcome_msg': "Hello Fast Campus"})

def redirect_test():
    pass