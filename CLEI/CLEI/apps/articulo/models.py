#encoding:utf-8
from django.db import models
from CLEI.apps.participante.models import Autor, MiembroComite

# Clase para el modelo de topicos
class Topico(models.Model):
    nombre_topico = models.CharField(max_length=50, primary_key=True, verbose_name='Nombre del Tópico')
    
    def __unicode__(self):
	return self.nombre_topico
	

# Clase para el modelo de articulos
class Articulo(models.Model):
    id_articulo = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título', help_text='Título del artículo')
    resumen = models.TextField()
    texto = models.TextField()
    autores = models.ManyToManyField(Autor, verbose_name='Autor(es)')
    topicos = models.ManyToManyField(Topico)
    aceptado = models.BooleanField(default=False)
    aceptado_especial = models.BooleanField(default=False)
    rechazado_falta_cupo = models.BooleanField(default=False)
    rechazado_por_promedio = models.BooleanField(default=False)
    p1 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 1')
    p2 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 2', blank=True)
    p3 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 3', blank=True)
    p4 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 4', blank=True)
    p5 = models.CharField(max_length=30, verbose_name = 'Palabra Clave 5', blank=True)
	    
    def __unicode__(self):
	return str(self.id_articulo)


# Clase para el modelo de puntuaciones a los articulos	
class Puntuacion(models.Model):
    correo = models.ForeignKey(MiembroComite)
    id_articulo = models.ForeignKey(Articulo)
    puntuacion = models.FloatField(default=0.0	, verbose_name='Puntuación')
    
    def __unicode__(self):
	return str(self.id_articulo)
	
    class Meta:
	unique_together = ("correo","id_articulo")