from django.shortcuts import render,redirect

from posts.forms import PostForm
from .models import Post
def post_home(request):
    post=Post.objects.all()
    return render(request,'post_home.html',{'post':post})

# Create your views here.
def create_post(request):
    if request.method=='POST':
        post=PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('pos/')
    else:
        post=PostForm()
        return render(request,'post_forms.html',{'post':post})
def up_post(request,id):
    p=Post.objects.get(id=id)
    if request.method == 'POST':
        post = PostForm(request.POST,instance=p)
        if post.is_valid():
            post.save()
            return redirect('pos/')
    else:
        post = PostForm(instance=p)
        return render(request, 'post_forms.html', {'post': post})
def del_p(request,id):
    Post.objects.get(id=id).delete()
    return redirect('pos/')
