from django.shortcuts import render,redirect

from myapp.models import Product
from myapp.forms import ProductForm
from posts.models import Post

# Create your views here.
def home(request):
    por=Product.objects.all()
    return render(request,'home.html',{'por':por})

