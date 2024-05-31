from . import forms
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic
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


class BookListView(generic.ListView):
    template_name = "books/books_list.html"
    model = Book
    context_object_name = "books"

    def get_queryset(self):
        return self.model.objects.all()

class BooksDetailView(generic.DetailView):
    template_name = "books/book_detail.html"
    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(Book, id=books_id)


class CreateReviewView(generic.CreateView):
    template_name = "books/create_review.html"
    form_class = forms.ReviewForm
    success_url = "/books"

    def form_valid(self, form):
        return super(CreateReviewView, self).form_valid(form=form)

class EditBookView(generic.UpdateView):
    template_name = "books/edit.html"
    form_class = forms.BookForm
    success_url = "/books"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(Book, id=book_id)

    def form_valid(self, form):
        return super(EditBookView, self).form_valid(form=form)

class DeleteBookView(generic.DeleteView):
    success_url = "/books"
    template_name = "books/delete.html"
    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(Book, id=book_id)

class CreateBookView(generic.CreateView):
    template_name = "books/create.html"
    form_class = forms.BookForm
    success_url = "/books"

    def form_valid(self, form):
        return super(CreateBookView, self).form_valid(form=form)
