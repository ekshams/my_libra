
# ************* function based views*******************

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader,RequestContext
from . models import *
from .form import BookForm
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    template = loader.get_template('index.html')
    context = {
        'books':Book.objects.all().order_by('subject'),
    }
    return HttpResponse(template.render(context,request))


def book(request, id):
    template = loader.get_template('book.html')
    context = {
        'book': Book.objects.get(id=id),
    }
    return HttpResponse(template.render(context,request))


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render(request))


def new_book(request):
    form = BookForm(request.POST or None)
    title = 'Add Book'
    context = {'title': title, 'form': form, }
    if form.is_valid():
        # print request.POST['subject']
        name = form.cleaned_data['name']
        author_name = form.cleaned_data['author_name']
        subject = form.cleaned_data['subject']
        instance = Book(name = name, author_name = author_name, subject = subject)
        instance.save()
        messages.success(request, 'The book has been added! ')
        return  redirect('home')
    template = 'new_book.html'
    return render(request, template,context)


def modify(request, id):
    title = 'Edit Book'
    data = Book.objects.get(id=id)
    form = BookForm(initial={'name': data.name, 'author_name': data.author_name, 'subject': data.subject})
    context = {'title': title, 'form': form, }
    form = BookForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        author_name = form.cleaned_data['author_name']
        subject = form.cleaned_data['subject']
        instance = Book(id=id, name=name, author_name=author_name, subject=subject)
        instance.save()
        messages.success(request, 'The book details has been modified! ')
        return redirect('home')
    template = 'modify_book.html'
    return render(request, template, context)


def delete(request, id):
    title = 'Book Deleted!'
    data = Book.objects.get(id=id)
    Book.objects.filter(id=id).delete()
    messages.add_message(request, messages.SUCCESS, 'The book has been deleted! ')
    return redirect('home')
