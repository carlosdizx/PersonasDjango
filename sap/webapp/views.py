from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    mensajes = {'mesnsaje': 'Valor 1','texto':'Valor 2'}
    return render(request, 'bienvenido.html', mensajes)
