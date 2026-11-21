from django.contrib import admin
from . models import vendorlogin


# Register your models here.
class formlogin(admin.ModelAdmin):
    list_display = ['name','address', 'area', 'contactno', 'email']
admin.site.register(vendorlogin)
