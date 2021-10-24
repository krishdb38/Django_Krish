from django.contrib import admin
from django.db import models
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ("email",)
    
admin.site.register(Fcuser, FcuserAdmin)