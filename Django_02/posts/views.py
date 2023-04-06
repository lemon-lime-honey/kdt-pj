from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


@login_required
def category(request, subject):
    posts = Post.objects.filter(category=subject)
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/new.html', context)


@login_required
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')


@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/edit.html', context)

