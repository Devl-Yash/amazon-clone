from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from . models import vendorlogin
from . form import formlogin

# Create your views here.
def login(request):
    if request.method == 'POST':
        forms = formlogin(request.POST, request.FILES)  
        if forms.is_valid():
            forms.save()
            return redirect('vendor')
    else :
        forms = formlogin()
    return render(request, 'vendorlogin.html',{'forms':forms})

