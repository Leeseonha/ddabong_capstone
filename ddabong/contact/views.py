from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.datetime.now()
            post.save()
            return redirect('create') 
    else:
        form = PostForm()
        posts = Post.objects.all()
        return render(request, 'create.html', {'form': form, 'posts': posts})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.datetime.now()
            post.save()
            return redirect('create') 
    else:
        form = PostForm(instance=post)
        return render(request, 'create.html', {'form': form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('create')

def views_donor(request):
    return render(request, 'views_donor.html')

def views_recipient(request):
    return render(request, 'views_recipient.html')