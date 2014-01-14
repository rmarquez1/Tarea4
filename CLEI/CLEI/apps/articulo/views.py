from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .forms import ArticuloForm, TopicoForm, PuntuacionForm
from .models import Articulo

# Create your views here.
def nuevo_articulo(request):
    if request.method == 'POST':
	formulario = ArticuloForm(request.POST)
	if formulario.is_valid():
	    formulario.save()
	    return HttpResponseRedirect('/admin')
    else:
	formulario = ArticuloForm()
    return render_to_response('articulo/crear_articulo.html', {'formulario':formulario}, context_instance= RequestContext(request))

def nuevo_topico(request):
    if request.method == 'POST':
	formulario = TopicoForm(request.POST)
	if formulario.is_valid():
	    formulario.save()
	    return HttpResponseRedirect('/admin')
    else:
	formulario = TopicoForm()
    return render_to_response('articulo/crear_topico.html', {'formulario':formulario}, context_instance= RequestContext(request))  
  
def asignar_puntuacion(request):
    if request.method == 'POST':
	formulario = PuntuacionForm(request.POST)
	if formulario.is_valid():
	    formulario.save()
	    return HttpResponseRedirect('/admin')
    else:
	formulario = PuntuacionForm()
    return render_to_response('articulo/asignar_puntuacion.html', {'formulario':formulario}, context_instance= RequestContext(request))
    