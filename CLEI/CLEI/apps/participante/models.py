#encoding:utf-8
from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    correo = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    inst_afil = models.CharField(max_length=30, verbose_name='Institución afiliada')
    
    class Meta:
	abstract = True

class Autor(Persona):
    pais = models.CharField(max_length=20)
    
    def __unicode__(self):
	return str(self.correo)
	
class MiembroComite(Persona):
    es_presidente = models.BooleanField()
    
    def hay_presidente(self):
	p = self.objects.filter(es_presidente=True).count()
	if p != 0:
	    return True
	return False
    
    def __unicode__(self):
	return str(self.correo)