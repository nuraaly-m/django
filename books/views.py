from . import forms
from django.shortcuts import render, get_object_or_404
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


def create_review_view(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Comment added')
    else:
        form = forms.ReviewForm()

    return render(request, template_name='books/create_review.html', context={'form': form})


def edit_book_view(request, id):
    book_id = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга изменена!')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='books/edit.html', context={'book_id': book_id,
                                                               'form': form})


def delete_book_view(request, id):
    book_id = get_object_or_404(Book, id=id)
    book_id.delete()
    return HttpResponse('Книга удалена')


def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга добавлена!')
    else:
        form = forms.BookForm()

    return render(request, template_name='books/create.html', context={'form': form})


