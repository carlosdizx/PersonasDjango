from django.shortcuts import render, get_object_or_404

from personas.models import Persona


def detallePersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle.html', {'persona': persona})
