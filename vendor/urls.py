from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.default, name = 'default'),
    path('vendor/',views.vendor, name = 'vendor'),
    path('details/<int:pk>/',views.details, name = 'details'),
]