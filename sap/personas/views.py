from django.shortcuts import render

from personas.models import Persona


def detallePersona(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'detalle.html', {'persona': persona})
