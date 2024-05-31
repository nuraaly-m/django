from django.urls import path
from .views import bio_view, hobby_view, datetime_view,book_list_view,book_detail_view


urlpatterns = [
    path('bio/', bio_view, name='bio'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', datetime_view, name='time'),
    path('books',book_list_view, name='books_list'),
    path('book/<int:id>',book_detail_view, name='book_detail'),
]