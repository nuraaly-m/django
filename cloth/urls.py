from django.urls import path
from .views import list_clothes,kids_clothes,men_clothes,women_clothes


urlpatterns = [
    path('clothes/', list_clothes, name='list_clothes'),
    path('kids_cloth/', kids_clothes, name='list_clothes'),
    path('women_cloth/',women_clothes, name='list_clothes'),
    path('men_cloth/',men_clothes, name='list_clothes'),
]
