from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    cantidad = Persona.objects.count()
    return render(request, 'bienvenido.html', {'cantidad': cantidad})
