from django.urls import path
from .views import ListClothesView,WomenClothes,KidsClothes,MenClothes


urlpatterns = [
    path('clothes/', ListClothesView.as_view(), name='list_clothes'),
    path('kids_cloth/', KidsClothes.as_view(), name='list_clothes'),
    path('women_cloth/',WomenClothes.as_view(), name='list_clothes'),
    path('men_cloth/',MenClothes.as_view(), name='list_clothes'),
]
