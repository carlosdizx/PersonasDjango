from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    return HttpResponse(f'Hola mundo, 2 + 2 = {2 + 2}')


def despedirse(request):
    return HttpResponse(f'Chao mundo, 2 + 2 = {2 + 2}')


def contacto(request):
    return HttpResponse('Datos de contacto, telefono: 3026508102 y correo: cediazb@siesa.com')
