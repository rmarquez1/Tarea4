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