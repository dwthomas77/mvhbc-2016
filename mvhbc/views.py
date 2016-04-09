from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'mvhbc/home.html', {});

def about(request):
    return render(request, 'mvhbc/about.html', {});

def resources(request):
    return render(request, 'mvhbc/resources.html', {});