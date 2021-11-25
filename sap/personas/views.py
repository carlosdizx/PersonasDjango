from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.models import Persona, Domicilio


def detalle_persona(request, ):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle.html', {'persona': persona})


PersonaForm = modelform_factory(Persona, exclude=[])


def nueva_persona(request):
    if request.method == 'POST':
        forma_persona = PersonaForm(request.POST)
        if forma_persona.is_valid():
            forma_persona.save()
            return redirect('index')
    else:
        forma_persona = PersonaForm()
    return render(request, 'nuevo.html', {'forma_persona': forma_persona})


def editar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        forma_persona = PersonaForm(request.POST, instance=persona)
        if forma_persona.is_valid():
            forma_persona.save()
            return redirect('index')
    else:
        forma_persona = PersonaForm(instance=persona)
    return render(request, 'editar.html', {'forma_persona': forma_persona})


def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')


def listar_domicilios(request):
    cantidad = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'listado_domicilios.html', {'cantidad': cantidad, 'domicilios': domicilios})
