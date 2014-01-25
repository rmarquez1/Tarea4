#encoding:utf-8
from django import forms
from .models import Clei

class CleiForm(forms.ModelForm):
	class Meta:
		model = Clei

	def clean_num_articulos(self):
		num = self.cleaned_data['num_articulos']

		if num < 0:
			raise forms.ValidationError("Dato inválido")
		return num


