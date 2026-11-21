from .models import dislogin
from django import forms

class login(forms.ModelForm):
    class Meta:
        model = dislogin
        fields = ['Name', 'Gender', 'ContactNo', 'Email', 'Address','Pincode']
