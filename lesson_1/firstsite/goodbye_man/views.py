from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def goodbye_man(request, *args, **kwargs):
    return HttpResponse(f'Goodbye, man')