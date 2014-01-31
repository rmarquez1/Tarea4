#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http      import HttpResponse, HttpResponseRedirect
from django.template  import RequestContext
from .forms import EventoForm, LugarForm, FechaForm, EventoSocialForm, EventoSimultaneoForm, DisponibilidadForm, AsignarLugarEventoSocialForm,AsignarLugarEventoSimultaneoForm
from .models import Evento, Lugar, Fecha, EventoSocial, EventoSimultaneo, AsignarLugarEventoSocial, Disponibilidad, AsignarLugarEventoSimultaneo

#Funcion para agregar las fechas que seran estipuladas para la conferencia
def crear_fecha(request):
   fechas = Fecha.objects.all()
   tamano = len(fechas)
   if tamano < 5:
      if request.method == 'POST':
         formulario = FechaForm(request.POST)
         if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/evento/calendario')
      else:
	        formulario = FechaForm()
      return render_to_response('evento/calendario.html',{'formulario':formulario},context_instance=RequestContext(request))
   else:
       return render_to_response('evento/max_fecha.html',{'fechas':fechas},context_instance=RequestContext(request))

#Funcion para añadir los eventos sociales
def evento_social(request):
    if request.method == 'POST':
	    formulario = EventoSocialForm(request.POST)
	    
	    if formulario.is_valid():
	       tipo_d     = request.POST['tipo_evento']
	       hora_d     = int(request.POST['hora_inicio'])
	       fecha_d    = request.POST['fecha']
	       duracion_d = int(request.POST['duracion'])
	       crear= Disponibilidad.objects.create(tipo_evento=tipo_d,hora = hora_d,fecha = fecha_d)
	       crear.save()
	       i = 1
	       while i<duracion_d:
	          hora_d = hora_d+1
	          crear = Disponibilidad.objects.create(tipo_evento=tipo_d,hora = hora_d,fecha = fecha_d)
	          crear.save()
  	          i= i+1
  	       formulario.save()
   	    return HttpResponseRedirect('/evento/social')
    else:
	      formulario = EventoSocialForm()
    return render_to_response('evento/evento_social.html',{'formulario':formulario}, context_instance= RequestContext(request))

#Función para los eventos de los articulos
def evento_simultaneo(request):
       
    if request.method == 'POST':
	    formulario = EventoSimultaneoForm(request.POST)
       
	    if formulario.is_valid():
	       nombre_d= request.POST['nombre_evento']
	       hora_d  = int(request.POST['hora_inicio'])
	       fecha_d = request.POST['fecha']
	       duracion_d = int(request.POST['duracion'])
	       crear= Disponibilidad.objects.create(tipo_evento = nombre_d,hora = hora_d,fecha=fecha_d)
	       crear.save()
	       i = 1
	       while i<duracion_d:
	          hora_d = hora_d+1
	          crear= Disponibilidad.objects.create(tipo_evento=nombre_d,hora = hora_d,fecha = fecha_d)
	          crear.save()
	          i = i+1
	       formulario.save()
	       return HttpResponseRedirect('/evento/simultaneo')
    else:
	      formulario = EventoSimultaneoForm()
    return render_to_response('evento/evento_simultaneo.html',{'formulario':formulario}, context_instance= RequestContext(request))

#Función para añadir lugares donde se presentara el evento
def nuevo_lugar(request):
    if request.method == 'POST':
	    formulario = LugarForm(request.POST)
	    
	    if formulario.is_valid():
	       formulario.save()
	       return HttpResponseRedirect('/evento/lugar')
    else:
	      formulario = LugarForm()
    return render_to_response('evento/agregar_lugar.html',{'formulario':formulario}, context_instance= RequestContext(request))

#Función para listar los eventos
def lista_evento(request):
    eventos = EventoSocial.objects.all()
    return render_to_response('evento/lista_eventos.html',{'eventos':eventos}, context_instance=RequestContext(request))

def lista_asignados(request):
    lista = Disponibilidad.objects.exclude(lugar = None)
    return render_to_response('evento/lista_asignados.html',{'lista':lista}, context_instance=RequestContext(request))

#Función para asignar lugar
def asignar_lugar(request):
   if request.method == 'POST':
      formulario = AsignarLugarEventoSocialForm(request.POST)
      if formulario.is_valid():
         tipo_d = request.POST['evento']
         lugar_d= request.POST['lugar']
         if Disponibilidad.objects.filter(tipo_evento=tipo_d,lugar = None).exists():
            Disponibilidad.objects.filter(tipo_evento=tipo_d,lugar = None).update(lugar=lugar_d)
            formulario.save()
            return HttpResponseRedirect('/evento/lugar/asignar')
         else:
            return render_to_response('evento/existe.html',context_instance= RequestContext(request))	 
         
   else:
	      formulario = AsignarLugarEventoSocialForm()
   return render_to_response('evento/asignar_lugar.html',{'formulario':formulario}, context_instance= RequestContext(request))

def asignar_lugar_simultaneo(request):
   if request.method == 'POST':
      formulario = AsignarLugarEventoSimultaneoForm(request.POST)
      if formulario.is_valid():
         tipo_d = request.POST['evento']
         lugar_d= request.POST['lugar']
         if Disponibilidad.objects.filter(tipo_evento=tipo_d,lugar = None).exists():
            Disponibilidad.objects.filter(tipo_evento=tipo_d,lugar = None).update(lugar=lugar_d)
            formulario.save()
            return HttpResponseRedirect('/evento/lugar/asignar_simultaneo')
         else:
            return render_to_response('evento/existe.html',context_instance= RequestContext(request))	 
         
   else:
	      formulario = AsignarLugarEventoSimultaneoForm()
   return render_to_response('evento/asignar_lugar.html',{'formulario':formulario}, context_instance= RequestContext(request))

