from django.urls import path
from .views import (bio_view, hobby_view, datetime_view,BookListView,BooksDetailView,EditBookView,
                    CreateBookView,CreateReviewView,DeleteBookView,SearchBookView)


urlpatterns = [
    path('bio/', bio_view, name='bio'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', datetime_view, name='time'),
    path('books',BookListView.as_view(), name='books_list'),
    path('book/<int:id>',BooksDetailView.as_view(), name='book_detail'),
    path('create_book',CreateBookView.as_view(), name='create_book'),
    path('edit_book/<int:id>',EditBookView.as_view(), name='book_edit'),
    path('delete_book/<int:id>',DeleteBookView.as_view(), name='book_edit'),
    path('create_review',CreateReviewView.as_view(), name='book_edit'),
    path('search_clothes',SearchBookView.as_view(), name='search_book'),
]
