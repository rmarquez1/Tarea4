from django.template import Context, loader
from apps.eventos.models import Evento
from django.http import HttpResponse

def generar_programa(request):
    eventos  = Evento.objects.all()
    eventos.order_by('fecha', 'inicio')
    template = loader.get_template('eventos/index.html')
    context  = Context({
        'eventos' : eventos,
    })
    return HttpResponse(template.render(context))

def mostrar(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    template = loader.get_template('eventos/mostrar.html')
    context = Context({
        'evento' : evento,
    })
    return HttpResponse(template.render(context))

