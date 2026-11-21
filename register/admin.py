from django.contrib import admin
from . models import dislogin
from . forms import login

# Register your models here.
class login(admin.ModelAdmin):
    list_display = ('Name', 'Gender', 'ContactNo', 'Email', 'Address', 'Pincode')
    search_fields = ('Name', 'Gender', 'Email',  'Address')
    list_filter = ('Gender')
admin.site.register(dislogin)