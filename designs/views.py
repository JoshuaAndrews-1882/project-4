from django.shortcuts import render
from django.http import HttpResponse


def designs(request):
    return render(request, 'designs/designs.html')


def design(request, pk):
    return render(request, 'designs/design.html')
