from . models import product
from django import forms

class formproduct(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'image', 'price']