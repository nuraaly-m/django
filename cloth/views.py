from django.shortcuts import render
from django.views import generic

from cloth.models import Cloth


# Create your views here.
class ListClothesView(generic.ListView):
    template_name = "cloth/list_cloth.html"
    context_object_name = "clothes"
    model = Cloth

    def get_queryset(self):
        return self.model.objects.all()

class KidsClothes(generic.ListView):
    template_name = "cloth/kids.html"
    context_object_name = "clothes"
    model = Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name__icontains='детская')

class WomenClothes(generic.ListView):
    template_name = "cloth/list_cloth.html"
    context_object_name = "clothes"
    model = Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name__icontains='женская')

class MenClothes(generic.ListView):
    template_name = "cloth/list_cloth.html"
    context_object_name = "clothes"
    model = Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name__icontains='мужская')

