from django import forms
from .models import Autor, MiembroComite


class AutorForm(forms.ModelForm):
    class Meta:
	model = Autor
	
class MiembroComiteForm(forms.ModelForm):
    class Meta:
	model = MiembroComite