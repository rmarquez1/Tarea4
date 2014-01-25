#encoding:utf-8
from django import forms
from .models import Articulo, Puntuacion, Topico


class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo

class TopicoForm(forms.ModelForm):
	class Meta:
		model = Topico

class PuntuacionForm(forms.ModelForm):
    class Meta:
		model = Puntuacion
	
    def clean_puntuacion(self):
		puntaje = self.cleaned_data['puntuacion']
	
		if puntaje<1.0 or puntaje>5.0:
			raise forms.ValidationError("El puntaje es de 1 a 5")
	
		return puntaje
