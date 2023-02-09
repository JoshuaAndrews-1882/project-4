from django.shortcuts import render
from django.http import HttpResponse
from .models import Design


def designs(request):
    designs = Design.objects.all()
    context = {'designs': designs}
    return render(request, 'designs/designs.html', context)


def design(request, pk):
    design = Design.objects.get(id=pk)
    return render(request, 'designs/design.html', {'design': design})


def createDesign(request):
    return render(request, "designs/design_form.html")