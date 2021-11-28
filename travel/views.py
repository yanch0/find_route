from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Heh'

    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'Meh'

    return render(request, 'about.html', {'name': name})