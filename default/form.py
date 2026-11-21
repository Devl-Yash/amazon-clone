from . models import vendorlogin
from django import forms

class formlogin(forms.ModelForm):
    class Meta:
        model = vendorlogin
        fields = ['name', 'address', 'area', 'contactno', 'email']