from django.contrib import admin
from .models import Student, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Student)