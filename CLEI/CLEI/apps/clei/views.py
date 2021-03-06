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
		num = clei.get_num_articulos()
		# Ciclo que recorre la lista de articulos que el presidente 
		# selecciono y lo ingresa a la lista de los aceptados
		for i in range(len(opcion)):
		    clei.set_aceptados(opcion[i])
		    Articulo.objects.filter(id_articulo=opcion[i]).update(aceptado_especial=True)
		    num -= 1
		lista_aceptados = clei.guardar_aceptados()
		return render_to_response('clei/mostrar_aceptados.html', 
			      {'lista_aceptados':lista_aceptados, 
			       'num': num},
			      context_instance= RequestContext(request))

# Vista donde se realiza la seleccion de articulos por un numero minimo por pais			      
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
		num_aux=p[0].num_articulos
		clei.set_num_articulos(p[0].num_articulos)
		lista_paises = clei.paises_conferencia()
		num_paises = len(lista_paises)
		valor = num_minimo_paises * num_paises
		num_articulos = clei.get_num_articulos()
		limite = clei.agregar_aceptados(num_minimo_paises)
		if limite != 0:
			clei.seleccionar_por_pais(num_minimo_paises)
		lista_aceptados = clei.guardar_aceptados()
		lista_empatados = clei.guardar_empatados()
		paises = []
		for i in range(len(lista_aceptados)):
			pais = lista_aceptados[i].autores.all()[0].pais
			paises.append(pais)
		if num_aux > len(clei.aceptables):
			limite = 0
		else:
			limite = clei.get_num_articulos()
		return render_to_response('clei/aceptados_empatados_pais.html',
		                     {'lista_aceptados':lista_aceptados,
		                    'limite': limite,
		                    'lista_empatados': lista_empatados,
		                    'num_articulos': num_articulos,
		                    'valor':valor,
		                    'paises': paises},
		                    context_instance= RequestContext(request))
	                        
	return render_to_response('clei/numero_minimo_paises.html',
	                    context_instance= RequestContext(request))
	                   
# Vista en la cual se muestran los estados finales de seleccion
def mostrar_estados_finales(request):
	clei.limpiar_falta_cupo()
	aceptados = clei.mostrar_aceptados()
	aceptados_especiales = clei.mostrar_aceptados_especiales()
	rechazados_promedio = clei.mostrar_rechazados_promedio()
	clei.asignar_falta_cupo()
	rechazados_falta_cupo = clei.mostrar_falta_cupo()
	tam_aceptados = len(aceptados)
	tam_acept_especiales = len(aceptados_especiales)
	tam_rec_promedios = len(rechazados_promedio)
	tam_rec_falta_cupo = len(rechazados_falta_cupo)
	return render_to_response('clei/estados_finales_seleccion.html',
		                     {'aceptados': aceptados,
		                      'aceptados_especiales': aceptados_especiales,
		                      'rechazados_promedio': rechazados_promedio,
		                      'rechazados_falta_cupo': rechazados_falta_cupo,
		                      'tam_aceptados': tam_aceptados,
		                      'tam_acept_especiales': tam_acept_especiales,
		                      'tam_rec_promedios': tam_rec_promedios,
		                      'tam_rec_falta_cupo': tam_rec_falta_cupo},
		                    context_instance= RequestContext(request))

# Vista que le indica al presidente cuales articulos participaran en la
# conferencia y a partir de alli pide al presidente que haga el desempate
def seleccion_por_pais_proporcion(request):
    clei.limpiar_aceptados()
    clei.limpiar_aceptables()
    clei.limpiar_empatados()
    clei.crear_articulos()
    p = Clei.objects.all()
    num = p[0].num_articulos
    clei.set_num_articulos(p[0].num_articulos)
    clei.crear_aceptables()
    limite = clei.seleccion_equitativa(p[0].num_articulos)
    lista_aceptados = clei.guardar_aceptados()
    lista_empatados = clei.guardar_empatados()
    return render_to_response('clei/aceptados_empatados.html',
                             {'lista_aceptados':lista_aceptados,
                              'limite': limite,
                              'lista_empatados': lista_empatados},
                              context_instance= RequestContext(request))

def seleccion_por_topico_proporcion(request):
    clei.limpiar_aceptados()
    clei.limpiar_aceptables()
    clei.limpiar_empatados()
    clei.crear_articulos()
    p = Clei.objects.all()
    clei.set_num_articulos(p[0].num_articulos)
    clei.crear_aceptables()
    limite = clei.seleccion_topicos(p[0].num_articulos)
    lista_aceptados = clei.guardar_aceptados()
    lista_empatados = clei.guardar_empatados()
    print clei.get_aceptables()
    return render_to_response('clei/aceptados_empatados.html',
                             {'lista_aceptados':lista_aceptados,
                              'limite': limite,
                              'lista_empatados': lista_empatados},
                              context_instance= RequestContext(request))
