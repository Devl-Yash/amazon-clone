from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from . models import product
from . form import formproduct


# Create your views here.
def default(request):
    user = product.objects.all()
    return render(request, 'default.html',{'user':user})

def vendor(request):
    if request.method == 'POST':
        form = formproduct(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('default')
    else :
        form = formproduct()
    return render(request, 'vendor.html',{'form':form})

def details(request, pk):
    t = get_object_or_404(product,pk = pk)
    return render(request, 'details.html',{'t':t})

