#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .clei import CLEI
from .forms import CleiForm
from .models import Clei
from CLEI.apps.articulo.models import Articulo, Topico, Puntuacion
# Create your views here.

# Se crea la clase clei
clei = CLEI()

def cantidad_articulos(request):
    if request.method == 'POST':
		formulario = CleiForm(request.POST)
		if formulario.is_valid():
			num = request.POST["num_articulos"]
			p = Clei.objects.all()
			if len(p) == 0:
				formulario.save()
			else:
				Clei.objects.all().update(num_articulos=num)
			return HttpResponseRedirect('/privado/presidente')
    else:
		formulario = CleiForm()
    return render_to_response('clei/numero_articulos.html', 
    						 {'formulario':formulario}, 
    						 context_instance= RequestContext(request))

# Vista que le indica al presidente el numero de articulos que habra en 
# conferencia y a partir de alli generar la lista de los aceptados_empatados
# y los empatados
def crear_aceptados_empatados(request):
	clei.limpiar_aceptados()
	clei.limpiar_aceptables()
	clei.limpiar_empatados()
	clei.crear_articulos()
	p = Clei.objects.all()
	clei.set_num_articulos(p[0].num_articulos)
	clei.crear_aceptables()
	promedios = clei.listar_promedios(clei.get_aceptables())
	limite = clei.crear_aceptados_empatados(promedios, clei.get_aceptables())
	lista_aceptados = clei.guardar_aceptados()
	lista_empatados = clei.guardar_empatados()
	print clei.get_aceptables()
	return render_to_response('clei/aceptados_empatados.html', 
			  		         {'lista_aceptados':lista_aceptados,
				       		  'limite': limite,
				       		  'lista_empatados': lista_empatados},
				      		  context_instance= RequestContext(request))
			      
			      
# Vista donde el presidente selecciona de la lista de empatados aquellos 
# que ingresara a la lista de aceptados
def seleccion_desempate(request): 
    if request.method == 'POST':
		opcion = request.POST.getlist("empatados")
		# Ciclo que recorre la lista de articulos que el presidente 
		# selecciono y lo ingresa a la lista de los aceptado
		for i in range(len(opcion)):
		    clei.set_aceptados(opcion[i])
		lista_aceptados = clei.guardar_aceptados()
		return render_to_response('clei/mostrar_aceptados.html', 
			      {'lista_aceptados':lista_aceptados},
			      context_instance= RequestContext(request))
			      
def seleccion_por_pais(request):
	clei.limpiar_aceptados()
	clei.limpiar_aceptables()
	clei.limpiar_empatados()
	# creamos la lista de los articulos aceptables
	if request.method == 'POST':
		num_minimo_paises = int(request.POST.get("minimo"))
		clei.crear_articulos()
		clei.crear_aceptables()
		p = Clei.objects.all()
		clei.set_num_articulos(p[0].num_articulos)
		lista_paises = clei.paises_conferencia()
		num_paises = len(lista_paises)
		#print 'num_paises: ', num_paises
		limite = clei.agregar_aceptados(num_minimo_paises)
		print 'limite: ', limite
		#print 'aceptados: ', clei.get_aceptados()
		if limite != 0:
			clei.seleccionar_por_pais(num_minimo_paises)
		lista_aceptados = clei.guardar_aceptados()
		lista_empatados = clei.guardar_empatados()
		#print 'lista empatados: ', lista_empatados
		#print 'lista aceptados: ', lista_aceptados
		limite = clei.get_num_articulos()
		print 'limite: ', limite
		return render_to_response('clei/aceptados_empatados.html',
		                     {'lista_aceptados':lista_aceptados,
		                    'limite': limite,
		                    'lista_empatados': lista_empatados,
		                    'numero_paises': num_paises},
		                    context_instance= RequestContext(request))
	                        
	return render_to_response('clei/numero_minimo_paises.html',
	                    context_instance= RequestContext(request))
