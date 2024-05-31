from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from books.models import Book


def bio_view(request):
    if request.method == 'GET':
        return HttpResponse('my name is nuraaly, i am 18')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('my hobby is reading')


def datetime_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())

def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        context = {'books': books,}
        return render(request,template_name='books/books_list.html',context=context)


def book_detail_view(request, id):
    if request.method == 'GET':
        book = Book.objects.get(id=id)
        context = {'book': book,}
        return render(request,'books/book_detail.html',context=context)

