from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import CustomUser, Staffs, Students, AdminHOD
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def loginUser(request):
    return render(request, "login_page.html")

def doLogin(request):
    print('here')
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    
    # user type 
    # user_type = request.GET.get('user_type')
    print(email_id, password, request.user)
    
    if not  ( email_id and password) :
        messages.error(request, "Invalid Login credentials")
        return render(request,"login_page.html")
    user = CustomUser.objects.filter(email = email_id, password = password).last()
    
    if not user:
        messages.error(request, "Invalid Login credentials") 
        return render(request, "login_page.html")
    login(request, user)
    print("user is " , user.user)
    print('user Type is', user.user_type)
    
    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home/')
    
    if user.user_type == CustomUser.STAFF:
        return redirect('staff_home/')
    
    if user.user_type == CustomUser.HOD:
        return redirect('admin_home/')
    
    return render(request, 'home.html')

def registration(request):
    return render(request,"registration.html")

def doRegistrtation(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email_id = request.GET.get('email_id')
    password = request.GET.get('password')
    confirm_password = request.GET.get('confirm_password')
    
    if not (email_id and password and confirm_password ):
        # if any blank then 
        messages.error(request, "Please provide all the required fields ")
        return render(request,'registration.html')
    # Check weather user exist or not 
    is_user_exist = CustomUser.objects.filter(email = email_id).exit() # True or False
    
    # if exist ask for another if not then register 
    if is_user_exist:
        messages.error(request, 'User with this email id already exists. Please Proceed to login')
        return render(request,'registration.html')
    
    user_type = get_user_type_from_emaill(email_id) # Function defined below
    
    if user_type is None:
        messages.error(request,'Please use valid format for the email id ')
        return render(request,'registration.html')
    
    username = email_id.split("@")[0].split('.')[0]
    if CustomUser.objects.filter(username = username).exists():
        messages.error(request,"User with this name already exists")
        return render(request, 'registration.html')
    # if all Condition full fill then we save info to db
    user = CustomUser()
    user.username = username
    user.email = email_id
    user.password = password
    user.first_name = first_name
    user.last_name = last_name
    user.save() # save in db
    
    
def logout_user(request):
    logout(request)
    
    return HttpResponseRedirect('/')

def get_user_type_from_email(email_id):
    """
    Returns Custom user user_type corresponding to the given email address.
    """
    
    try:
        email_id = email_id.split('@')[0] # id 
        email_user_type = email_id.split('.')[1]
        return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
    except:
        None