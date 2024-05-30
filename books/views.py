from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def bio_view(request):
    if request.method == 'GET':
        return HttpResponse('my name is nuraaly, i am 18')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('my hobby is reading')


def datetime_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


