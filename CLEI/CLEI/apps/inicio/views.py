from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from CLEI.apps.participante.models import Autor, MiembroComite
from CLEI.apps.participante.forms import AutorForm, InscritoForm

# Create your views here.
def inicio(request):
    return render_to_response('inicio/inicio.html', context_instance= RequestContext(request))

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    p = MiembroComite.objects.filter(username=usuario, es_presidente=True)
                    if len(p)!=0:
            			return HttpResponseRedirect('/privado/presidente')
                    else:
                        return HttpResponseRedirect('/privado/miembro')
                else:
                    return HttpResponse('No esta activo')
            else:
                return HttpResponse('No existe ese usuario')
    else:
        formulario = AuthenticationForm()
    return render_to_response('inicio/ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

def registrar(request):
    if request.method == 'POST':
		formulario = InscritoForm(request.POST)
		if formulario.is_valid():
		    formulario.save()
		    return HttpResponseRedirect('/')
    else:
		formulario = InscritoForm()
    return render_to_response('inicio/registrar.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def privado_presidente(request):
    usuario = request.user
    return render_to_response('inicio/inicio_presidente.html', {'usuario':usuario}, context_instance=RequestContext(request))
    
@login_required(login_url='/ingresar')
def privado_miembro(request):
    usuario = request.user
    return render_to_response('inicio/inicio_miembro.html', {'usuario':usuario}, context_instance=RequestContext(request))
    
@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')