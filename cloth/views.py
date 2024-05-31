from django.shortcuts import render

from cloth.models import Cloth


# Create your views here.

def list_clothes(request):
    clothes = Cloth.objects.all()
    context = {'clothes': clothes}
    return render(request,template_name='cloth/list_cloth.html',context=context)

def kids_clothes(request):
    clothes = Cloth.objects.filter(tags__name__icontains='детская')
    context = {'clothes': clothes}
    return render(request,template_name='cloth/kids.html',context=context)

def women_clothes(request):
    clothes = Cloth.objects.filter(tags__name__icontains='женская')
    context = {'clothes': clothes}
    return render(request,template_name='cloth/list_cloth.html',context=context)

def men_clothes(request):
    clothes = Cloth.objects.filter(tags__name__icontains='мужская')
    context = {'clothes': clothes}
    return render(request,template_name='cloth/list_cloth.html',context=context)
