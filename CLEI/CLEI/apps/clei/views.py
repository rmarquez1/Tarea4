from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .clei import Clei
from CLEI.apps.articulo.models import Articulo, Topico, Puntuacion
# Create your views here.
# Metodo que devuelve una lista de los articulos considerados como aceptables
clei = Clei()
def numero_articulos(request):
    # creamos la lista de los articulos aceptables
    if request.method == 'POST':
	num = int(request.POST.get("articulos"))
	clei.set_num_articulos(num)
	clei.crear_articulos()
	clei.crear_aceptables()
	promedios = clei.listar_promedios(clei.get_aceptables())
	limite = clei.crear_aceptados_empatados(promedios, clei.get_aceptables())
	lista_aceptados = clei.guardar_aceptados()
	lista_empatados = clei.guardar_empatados()
	return render_to_response('clei/aceptados_empatados.html', 
			      {'lista_aceptados':lista_aceptados,
			       'limite': limite,
			       'lista_empatados': lista_empatados},
			      context_instance= RequestContext(request))
			      
    return render_to_response('clei/numero_articulos.html', 
			      context_instance= RequestContext(request))
			      
def crear_aceptados_empatados(request): 
    if request.method == 'POST':
	opcion = request.POST.getlist("empatados")
	#print opcion
	for i in range(len(opcion)):
	    clei.set_aceptados(opcion[i])
	#print clei.get_aceptados()
	lista_aceptados = clei.guardar_aceptados()
	return render_to_response('clei/mostrar_aceptados.html', 
			      {'lista_aceptados':lista_aceptados},
			      context_instance= RequestContext(request))