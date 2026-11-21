from django.contrib import admin
from . models import product


# Register your models here.
class formproduct(admin.ModelAdmin):
    list_display = ['name', 'image', 'price']
admin.site.register(product)

