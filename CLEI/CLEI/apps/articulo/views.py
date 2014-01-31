from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .forms import ArticuloForm, TopicoForm, PuntuacionForm
from .models import Articulo
from CLEI.apps.participante.models import MiembroComite

# Create your views here.
def nuevo_articulo(request):
    if request.method == 'POST':
		formulario = ArticuloForm(request.POST)
		if formulario.is_valid():
		    formulario.save()
		    return HttpResponseRedirect('/articulo/create')
    else:
		formulario = ArticuloForm()
    return render_to_response('articulo/crear_articulo.html', {'formulario':formulario}, context_instance= RequestContext(request))

def nuevo_topico(request):
    if request.method == 'POST':
		formulario = TopicoForm(request.POST)
		if formulario.is_valid():
		    formulario.save()
		    return HttpResponseRedirect('/articulo/topico/create')
    else:
		formulario = TopicoForm()
    return render_to_response('articulo/crear_topico.html', {'formulario':formulario}, context_instance= RequestContext(request))  
  
def asignar_puntuacion_presidente(request):
    if request.method == 'POST':
		formulario = PuntuacionForm(request.POST)
		if formulario.is_valid():
			id = request.POST["correo"]
			usuario = MiembroComite.objects.filter(id=id)[0].username
			esta_autenticado = str(request.user) == usuario
			print esta_autenticado
			if esta_autenticado:
			    formulario.save()
			return render_to_response('articulo/resultado_puntuacion_presidente.html', 
			  		         {'esta_autenticado': esta_autenticado},
				      		  context_instance= RequestContext(request))
    else:
		formulario = PuntuacionForm()
    return render_to_response('articulo/asignar_puntuacion_presidente.html', {'formulario':formulario}, context_instance= RequestContext(request))

    
def asignar_puntuacion_miembro(request):
    if request.method == 'POST':
		formulario = PuntuacionForm(request.POST)
		if formulario.is_valid():
			id = request.POST["correo"]
			usuario = MiembroComite.objects.filter(id=id)[0].username
			esta_autenticado = str(request.user) == usuario
			print esta_autenticado
			if esta_autenticado:
			    formulario.save()
			return render_to_response('articulo/resultado_puntuacion_miembro.html', 
			  		         {'esta_autenticado': esta_autenticado},
				      		  context_instance= RequestContext(request))
    else:
		formulario = PuntuacionForm()
    return render_to_response('articulo/asignar_puntuacion_miembro.html', {'formulario':formulario}, context_instance= RequestContext(request))
    
# Metodo que devuelve una lista de los articulos considerados como aceptables
#def crear_aceptables(request):
    ## creamos la lista de los articulos aceptables
    #articulo=ArticuloForm()
    #aceptables= articulo.get_aceptables()
    #return render_to_response('articulo/mostrar_aceptables.html', {'aceptables':aceptables}, context_instance= RequestContext(request))