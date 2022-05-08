from django.contrib import admin
from .models import Position

from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

class PositionResource(resources.ModelResource):
    invoice = Field()
    class Meta:
        model = Position
        fields = ('id', "invoice", "title", "description", "amount", "created")

    def dehydrate_invoice(self, obj):
        return obj.invoice.number

class PositionAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PositionResource


# Register your models here.
admin.site.register(Position, PositionAdmin)