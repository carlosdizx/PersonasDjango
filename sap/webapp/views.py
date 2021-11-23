from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    return HttpResponse(f'Hola mundo {2+2}')
