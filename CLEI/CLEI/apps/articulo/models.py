#encoding:utf-8
from django.db import models
from CLEI.apps.participante.models import Autor, MiembroComite

class Topico(models.Model):
    nombre_topico = models.CharField(max_length=50, primary_key=True, verbose_name='Nombre del Tópico')
    
    def __unicode__(self):
	return self.nombre_topico
	
# Create your models here.
class Articulo(models.Model):
    id_articulo = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título', help_text='Título del artículo')
    resumen = models.TextField()
    texto = models.TextField()
    autores = models.ManyToManyField(Autor, verbose_name='Autor(es)')
    topicos = models.ManyToManyField(Topico)
    p1 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 1')
    p2 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 2', blank=True)
    p3 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 3', blank=True)
    p4 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 4', blank=True)
    p5 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 5', blank=True)
    # COLOCAR ESTADOS DE SELECCION
    

		    
    def __unicode__(self):
	return str(self.id_articulo)
	
class Puntuacion(models.Model):
    correo = models.ForeignKey(MiembroComite)
    id_articulo = models.ForeignKey(Articulo)
    puntuacion = models.FloatField(default=0.0	, verbose_name='Puntuación')
    
    def __unicode__(self):
	return str(self.id_articulo)
	
    class Meta:
	unique_together = ("correo","id_articulo")