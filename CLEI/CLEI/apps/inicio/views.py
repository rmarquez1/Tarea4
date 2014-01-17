from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def inicio(request):
    return render_to_response('inicio/inicio.html', context_instance= RequestContext(request))