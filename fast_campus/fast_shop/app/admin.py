from django.contrib import admin
from app import models as m # all models are here
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.admin import  AdminSite
# from django.utils.translation import ugettext_lazy

## 
admin.site.site_header = "FastShop Admin"
admin.site.site_title = "Krishna"
admin.site.index_title = "FastShop Admin Examples "

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ("content")

# Register your models here.
admin.site.register(m.User)

