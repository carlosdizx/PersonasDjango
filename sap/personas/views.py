from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404

from personas.models import Persona


def detalle_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle.html', {'persona': persona})


PersonaForm = modelform_factory(Persona,exclude=[])


def nueva_persona(request):
    forma_persona = PersonaForm()
    return render(request, 'nuevo.html', {'forma_persona': forma_persona})
