#encoding:utf-8
from django import forms
from .models import Autor, MiembroComite, Inscrito


class AutorForm(forms.ModelForm):
    class Meta:
	model = Autor

class MiembroComiteForm(forms.ModelForm):
    class Meta:
	model = MiembroComite
	
    def clean_es_presidente(self):
	existe = self.cleaned_data['es_presidente']
	
	if existe==True:
	    p = MiembroComite.objects.filter(es_presidente=True).count()
	
	    if p == 1:
		raise forms.ValidationError("Ya existe Presidente en el comité")
	
	return existe


class InscritoForm(forms.ModelForm):
	class Meta:
		model = Inscrito
