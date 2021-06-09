from django.shortcuts import render, HttpResponse, redirect
from .models import books,authors

def book(request):
    context = {
    "books": books.objects.all(),
    "authors": authors.objects.all(),
    }
    return render(request,"book.html",context)

def add_new_book(request):
    books.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

def author(request):
    context = {
    "authors": authors.objects.all(),
    }
    return render(request,"author.html",context)

def add_new_author(request):
    authors.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],notes=request.POST['notes'])
    return redirect('/authors')

def books_details(request,id):
    book = books.objects.get(id= id)
    context = {
    "book": book,
    "books": books.objects.all(),
    "authors" : book.authors.all,
    "allauthors": authors.objects.all(),
    }
    return render(request,'book_details.html',context)

def authors_details(request,id):
    author = authors.objects.get(id= id)
    context = {
    "author": author,
    "authors": authors.objects.all(),
    "books" : author.book.all,
    "allbooks": books.objects.all(),
    }
    return render(request,'author_details.html',context)

def add_author(request,id):
    book = books.objects.get(id= id)
    auth = request.POST['authors']
    author = authors.objects.get(id = auth)
    book.authors.add(author)
    return redirect("/books/"+str(id))

def add_book(request,id):
    author = authors.objects.get(id= id)
    book = request.POST['books']
    booki = books.objects.get(id = book)
    author.book.add(booki)
    return redirect("/authors/"+str(id))