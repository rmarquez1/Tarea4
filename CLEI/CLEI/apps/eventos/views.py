from django.template import Context, loader
from .models import Evento
from CLEI.apps.evento.models import EventoSocial
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def generar_programa(request):
    eventos  = EventoSocial.objects.all()
    eventos.order_by('fecha', 'inicio')
    return render_to_response('eventos/index.html', 
    						 {'eventos':eventos}, 
    						 context_instance= RequestContext(request))

def mostrar(request, evento_tipo_evento):
    evento = EventoSocial.objects.get(tipo_evento=evento_tipo_evento)
    return render_to_response('eventos/mostrar.html', 
    						 {'evento':evento}, 
    						 context_instance= RequestContext(request))

