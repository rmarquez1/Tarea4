from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Autor, MiembroComite
from .forms import AutorForm, MiembroComiteForm
# Create your views here.
#def usuarios(request):
    #usuarios = User.objects.all()
    #return render_to_response('participante/usuarios.html',{'usuarios':usuarios}, context_instance=RequestContext(request))

def nuevo_miembro(request):
    if request.method == 'POST':
		formulario = MiembroComiteForm(request.POST)
		if formulario.is_valid():
		    username = formulario.cleaned_data['username']
		    password = formulario.cleaned_data['password']
		    correo = formulario.cleaned_data['correo']
		    user = User.objects.create_user(username, correo, password)
		    user.is_active = True
		    user.save()
		    formulario.save()
		    return HttpResponseRedirect('/participante/miembro/create')
    else:
		formulario = MiembroComiteForm()
    return render_to_response('participante/crear_miembro.html', 
			      {'formulario':formulario},
			      context_instance= RequestContext(request))
   
   
def nuevo_autor(request):
    if request.method == 'POST':
		formulario = AutorForm(request.POST)
		if formulario.is_valid():
		    formulario.save()
		    return HttpResponseRedirect('/participante/autor/create')
    else:
		formulario = AutorForm()
    return render_to_response('participante/crear_autor.html', {'formulario':formulario}, context_instance= RequestContext(request))

    