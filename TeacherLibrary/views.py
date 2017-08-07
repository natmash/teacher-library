from django.http import Http404
from django.shortcuts import render
from .models import Book
from django.template import RequestContext

def all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})