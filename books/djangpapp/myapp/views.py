from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StuForm, EmployeeForm

# Create your views here.
def hello(request):
    return HttpResponse('<h2> Hello Welcome to Django </h2>')

def index(request):
    stu = StuForm()
    content = {'form':stu}
    return render(request,'myapp/index.html', content)

def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    
    content ={'form': EmployeeForm()}
    return render(request,'myapp/emp.html',content)
        