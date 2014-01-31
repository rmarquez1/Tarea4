#encoding:utf-8
from django.db import models

#Lista de opciones para los tipos de eventos que se realizan simultaneamente
#para presentar articulos
EVENTO_ARTICULO_CHOICES =(
      ('Taller','Taller'),
      ('Sesiones de Ponencias','Sesiones de Ponencias'),
)

#Lista de eventos sociales
EVENTO_SOCIALES_CHOICES =(
      ('Apertura','Apertura'),
      ('Clausura','Clausura'),
      ('Eventos Sociales','Eventos Sociales'),
      ('Charlas Invitadas','Charlas Invitadas'),
)

HORA_INICIO_CHOICES =(
      (7 ,'7:00  a.m'),
      (8 ,'8:00  a.m'),
      (9 ,'9:00  a.m'),
      (10,'10:00 a.m'),
      (11,'11:00 a.m'),
      (12,'12:00 a.m'),
      (13,'1:00  p.m'),
      (14,'2:00  p.m'),
      (15,'3:00  p.m'),
      (16,'4:00  p.m'),
      (17,'5:00  p.m')
)

DURACION_CHOICES = (
      (1,'1 hr'),
      (2,'2 hrs'),
      (3,'3 hrs'),
      (4,'4 hrs'),
      (5,'5 hrs')
)
 
#Clase fecha
class Fecha(models.Model):
   dia = models.DateField(primary_key=True, verbose_name = 'Fecha: ')
   def __unicode__(self):
       return str(self.dia)
   class Meta:
       ordering = ["dia"]

#Clase abstracta Evento   
class Evento(models.Model):
   fecha       = models.ForeignKey(Fecha)
   hora_inicio = models.IntegerField(choices=HORA_INICIO_CHOICES, null=False, verbose_name = 'Hora de inicio')
   duracion    = models.IntegerField(choices=DURACION_CHOICES, null=False, verbose_name = 'Duración')
   class Meta:
       abstract = True

#Clase para los eventos sociales
class EventoSocial(Evento):
   tipo_evento = models.CharField(primary_key=True,max_length=30, choices=EVENTO_SOCIALES_CHOICES, verbose_name ='Tipo de Evento')
   def __unicode__(self):
       return self.tipo_evento


#Clase para los eventos de presentacion de articulos
class EventoSimultaneo(Evento):
   nombre_evento = models.CharField(primary_key=True,max_length=100, verbose_name = 'Indique El Nombre Del Evento ' )
   tipo_evento = models.CharField(max_length=30, choices=EVENTO_ARTICULO_CHOICES,verbose_name='Tipo de Evento ')
   def __unicode__(self):
       return self.nombre_evento

#Clase definida para los lugares
class Lugar(models.Model):


   nombre    = models.CharField(primary_key=True,max_length = 100,verbose_name= 'Nombre del Lugar')
   ubicacion = models.TextField(verbose_name='Ubicacion') #Pais
   cap_max   = models.PositiveIntegerField(blank=True,null=True)

   def __unicode__(self):
      return unicode(self.nombre)

#Asignar lugares      
class AsignarLugarEvento(models.Model):
   id_asig= models.AutoField(primary_key=True)
   lugar  = models.ForeignKey(Lugar)

   def __unicode__(self):
       return unicode(self.id_asig)
   class Meta:
       abstract = True

#Asignar lugares  
class AsignarLugarEventoSocial(AsignarLugarEvento):
   evento = models.ForeignKey(EventoSocial)

   def __unicode__(self):
       return unicode(self.id_asig)
   class Meta:
        unique_together = ("evento","lugar")

#Asignar lugares 
class AsignarLugarEventoSimultaneo(AsignarLugarEvento):
   evento = models.ForeignKey(EventoSimultaneo)
   def __unicode__(self):
       return unicode(self.id_asig)
   class Meta:
        unique_together = ("evento","lugar")


#Clase para la disponibilidad
class Disponibilidad(models.Model):
   id_disponi  = models.AutoField(primary_key=True)
   tipo_evento = models.CharField(max_length=50)
   hora        = models.IntegerField(blank=True,null=True)
   fecha       = models.DateField()
   lugar       = models.CharField(max_length=50,blank=True,null=True)
   
   def __unicode__(self):
       return unicode(self.id_disponi)
   class Meta:
        unique_together = ("tipo_evento","hora","fecha","lugar")
