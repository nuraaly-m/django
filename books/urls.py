from django.urls import path
from .views import (bio_view, hobby_view, datetime_view,book_list_view,book_detail_view,create_book_view,edit_book_view,
                    create_review_view,delete_book_view)


urlpatterns = [
    path('bio/', bio_view, name='bio'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', datetime_view, name='time'),
    path('books',book_list_view, name='books_list'),
    path('book/<int:id>',book_detail_view, name='book_detail'),
    path('create_book',create_book_view, name='create_book'),
    path('edit_book/<int:id>',edit_book_view, name='book_edit'),
    path('delete_book/<int:id>',delete_book_view, name='book_edit'),
    path('create_review',create_review_view, name='book_edit'),
]