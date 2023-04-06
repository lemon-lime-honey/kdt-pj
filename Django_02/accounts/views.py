from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
           auth_login(request, form.get_user())
           return redirect('posts:index')
    else:
      form = AuthenticationForm()
    context = {
       'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
   auth_logout(request)
   return redirect('posts:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           auth_login(request, user)
           return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
      'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
   request.user.delete()
   return redirect('accounts:index')


@login_required
def update(request):
    if request.method == 'POST':
      form = CustomUserChangeForm(request.user, request.POST)
      if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
       'form': form,
    }
    return render(request, 'accounts/update.html', context)