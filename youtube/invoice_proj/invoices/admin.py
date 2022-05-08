import profile
from turtle import position
from django.contrib import admin
from .models import Invoice, Tag
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

class TagResource(resources.ModelResource):
    

    class Meta:
        model = Tag
        fields = ('id', 'name')

class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResource

class InvoiceResource(resources.ModelResource):
    profile = Field()
    receiver = Field()
    created = Field()

    class Meta:
        model = Invoice
        fields = ("id", "profile", "number", 'receiver',"completion_date", 'issue_date',
            "payment_date", "created", "closed", 'positions')

    def dehydrate_profile(self, obj):
        return obj.profile.user.username

    def dehydrate_receiver(self, obj):
        return obj.receiver.name # name from receiver table

    def dehydrate_created(self, obj):
        # dauy only
        return obj.created.strftime('%d-%m-%y')

    def dehydrate_closed(self, obj):
        if obj.closed == True:
            return "True"
        else :
            return "False"

    def dehydrate_positions(self, obj):
        positions_list = [x.title for x in obj.positions]
        positions_string = ', '.join(positions_list)
        return positions_string


class InvoiceAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = InvoiceResource


# Register your models here.
admin.site.register(Invoice , InvoiceAdmin)
admin.site.register(Tag, TagAdmin )