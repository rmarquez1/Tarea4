#encoding:utf-8
from  django  import forms
from  .models import Evento, Lugar, Fecha, EventoSocial, EventoSimultaneo, AsignarLugarEventoSocial, Disponibilidad, AsignarLugarEventoSimultaneo

class EventoForm(forms.ModelForm):
    class Meta:
	      model = Evento

class EventoSocialForm(forms.ModelForm):
    class Meta:
	      model = EventoSocial

class EventoSimultaneoForm(forms.ModelForm):
    class Meta:
	      model = EventoSimultaneo

class LugarForm(forms.ModelForm):
    class Meta:
	      model = Lugar

class FechaForm(forms.ModelForm):
    class Meta:
      	model = Fecha

class AsignarLugarEventoSocialForm(forms.ModelForm):
    class Meta:
         model = AsignarLugarEventoSocial

class AsignarLugarEventoSimultaneoForm(forms.ModelForm):
    class Meta:
         model = AsignarLugarEventoSimultaneo

class DisponibilidadForm(forms.ModelForm):
   class Meta:
         model = Disponibilidad
