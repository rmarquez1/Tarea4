from .models import Evento
from django.contrib import admin

class EventoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields' : ['nombre', 'tipo']}),
        ('Horario',         {'fields' : ['fecha', 'inicio', 'duracion']}),
    ]
    list_display = ('nombre', 'tipo', 'fecha', 'inicio',  'duracion')

admin.site.register(Evento, EventoAdmin)
