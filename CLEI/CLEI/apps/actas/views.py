from django.template import Context, loader
from eventos.models import Evento
from django.http import HttpResponse

def generar_acta(request, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    template = loader.get_template('actas/mostrar.html')
    context = Context({
	'articulo' : articulo,
    })
    return HttpResponse(template.render(context))

