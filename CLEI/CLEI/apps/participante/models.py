#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    username = models.CharField(max_length=30, unique=False)
    password = models.CharField(max_length=60, unique=False)
    correo = models.EmailField(unique=False)
    nombre = models.CharField(max_length=30, unique=False)
    apellido = models.CharField(max_length=30, unique=False)
    inst_afil = models.CharField(max_length=30, unique=False, verbose_name='Institución afiliada')
    
    class Meta:
	abstract = True
	unique_together = ("username", "correo")


class Autor(Persona):
    pais = models.CharField(max_length=20)
    
    def __unicode__(self):
	return str(self.correo)



class MiembroComite(Persona):
    es_presidente = models.BooleanField()
    
    def __unicode__(self):
	return str(self.correo)

class Inscrito(Persona):
    url = models.CharField(blank=True, null=True, max_length=100, unique=False)
    telefono = models.BigIntegerField(unique=False)

    def __unicode__(self):
		return str(self.correo)