from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from CLEI.apps.articulo.models import Articulo

def generar_acta(request):
    articulos = Articulo.objects.all()
    return render_to_response('actas/mostrar.html'	, 
    						 {'articulos':articulos}, 
    						 context_instance= RequestContext(request))

