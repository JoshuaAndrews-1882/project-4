from django.shortcuts import render
from django.http import HttpResponse


def designs(request):
    return HttpResponse('Here are the designs')


def design(request, pk):
    return HttpResponse('User design')