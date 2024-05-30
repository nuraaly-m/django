from django.urls import path
from .views import bio_view, hobby_view, datetime_view


urlpatterns = [
    path('bio/', bio_view, name='bio'),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', datetime_view, name='time'),
]