from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from . models import dislogin
from . forms import login

# Create your views here.
def admin(request):
    if request.method == 'POST':
        form = login(request.POST,request.FILES)
        if form.is_valid ():
            form.save()
            return redirect('default')
    else:
        form = login()
    return render(request, 'admin.html',{'form':form})
