from django.shortcuts import render, redirect

from myapp.models import Product
from myapp.forms import ProductForm


def create(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succed')
    else:
        form=ProductForm()
        return render(request,'forms.html',{'form':form})
def succed(request):
    return render(request, 'success.html')

def delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/')

def update(request,id):
    p=Product.objects.get(id=id)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ProductForm(instance=p)
        return render(request,'forms.html',{'form':form})