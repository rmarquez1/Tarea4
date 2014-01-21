from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .clei import Clei
from CLEI.apps.articulo.models import Articulo, Topico, Puntuacion
# Create your views here.
# Metodo que devuelve una lista de los articulos considerados como aceptables
def mostrar_aceptables(request):
    # creamos la lista de los articulos aceptables
    num = request.POST
    print num
    num_articulos = int(num['articulos'])
    clei=Clei(num_articulos)
    clei.crear_aceptables()
    promedios = clei.listar_promedios(clei.get_aceptables())
    limite = clei.crear_aceptados_empatados(promedios, clei.get_aceptables())
    lista_aceptados = clei.guardar_aceptados()
    lista_empatados = clei.guardar_empatados()
    return render_to_response('articulo/mostrar_aceptables.html', 
			      {'lista_aceptados':lista_aceptados,
			       'lista_empatados': lista_empatados},
			      context_instance= RequestContext(request))
			      