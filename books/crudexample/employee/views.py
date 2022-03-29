from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
        content = {'form' : form}
        
    return render(request, 'employee/index.html', content)

def show(request):
    employees = Employee.objects.all()
    content = {'employees':employees}
    return render(request, 'employee/show.html', content)


def edit(request, pk):
    employee = Employee.objects.get(id=pk)
    content =  {'employee': employee}
    return render(request, 'employee/edit.html',content) 

def update(request, pk):
    employee = Employee.objects.get(id = pk)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
    
    