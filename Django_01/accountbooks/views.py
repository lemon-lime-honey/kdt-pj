from django.shortcuts import render, redirect
from .models import AccountBook


def index(request):
    accountbooks = AccountBook.objects.all()
    context = {
        'accountbooks': accountbooks,
    }

    return render(request, 'accountbooks/index.html', context)


def detail(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    note = request.POST.get('note')
    description = request.POST.get('description')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')

    accountbook = AccountBook.objects.create(note = note, description = description, category = category, amount = amount, date = date)

    return redirect('accountbooks:detail', accountbook.pk)


def edit(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    accountbook.note = request.POST.get('note')
    accountbook.description = request.POST.get('description')
    accountbook.category = request.POST.get('category')
    accountbook.amount = request.POST.get('amount')
    accountbook.date = request.POST.get('date')

    accountbook.save()

    return redirect('accountbooks:detail', accountbook.pk)


def delete(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    accountbook.delete()
    return redirect('accountbooks:index')


def copy(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    
    accountbook.pk = None
    accountbook.save()
    return redirect('accountbooks:index')