#encoding:utf-8

from django.contrib import admin
from .models import Evento, Lugar, Fecha, EventoSocial, EventoSimultaneo,AsignarLugarEventoSocial,AsignarLugarEventoSimultaneo,Disponibilidad

admin.site.register(EventoSocial)
admin.site.register(EventoSimultaneo)
admin.site.register(Lugar)
admin.site.register(Fecha)
admin.site.register(AsignarLugarEventoSocial)
admin.site.register(AsignarLugarEventoSimultaneo)
admin.site.register(Disponibilidad)

