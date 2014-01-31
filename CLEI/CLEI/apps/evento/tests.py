#encoding:utf-8

from django.test import TestCase
from .models import Evento, Lugar, Fecha, EventoSocial, EventoSimultaneo, AsignarLugarEventoSocial, Disponibilidad, AsignarLugarEventoSimultaneo

class EventoTest(TestCase):

   def setUp(self):      
      
      #---------------------------------------------------
      # Creando Fecha
      #---------------------------------------------------
      
      fecha_1 = Fecha.objects.create(dia = '1/02/2014')
      fecha_2 = Fecha.objects.create(dia = '2/02/2014')
      fecha_3 = Fecha.objects.create(dia = '3/02/2014')
      fecha_4 = Fecha.objects.create(dia = '4/02/2014')

      #--------------------------------------------------
      # Creando Evento simultaneo
      #--------------------------------------------------
      
      even_1 = EventoSimultaneo.objects.create(nombre = 'Ponencia de computación')
      even_2 = EventoSimultaneo.objects.create(nombre = 'Taller de redes')
      even_3 = EventoSimultaneo.objects.create(nombre = 'Ponencia de ingenieria')
      
      #--------------------------------------------------
      # Creando Lugares
      #--------------------------------------------------
      lug_1 = Lugar.objects.create(nombre='Sala A', ubicacion = 'MYS-001', cap_max = 100)
      lug_2 = Lugar.objects.create(nombre='Sala B', ubicacion = 'MYS-002', cap_max = 250)
      lug_2 = Lugar.objects.create(nombre='Sala C', ubicacion = 'MYS-003', cap_max = 500)
      
      def test_crear_lugar(self):
         lugares = Lugar.objects.all()
         self.assertEquals('Sala A',lugares[0].nombre)
         self.assertEquals('Sala B',lugares[1].nombre)
         self.assertEquals('Sala C',lugares[2].nombre)
         self.assertEquals('MYS-001',lugares[0].ubicacion)
         self.assertEquals('MYS-002',lugares[1].ubicacion)
         self.assertEquals('MYS-003',lugares[2].ubicacion)
         self.assertEquals(500,lugares[2].cap_max)
      
      def test_fechas(self):
         fe = Fecha.objects.all()
         self.assertEquals('1/02/2014',fe[0].dia)
         self.assertEquals('2/02/2014',fe[1].dia)
         self.assertEquals('3/02/2014',fe[2].dia)
     
      def test_comp_evento(self):
         evens = EventoSimultaneo.objects.all()
         self.assertEquals('Ponencia de computación',evens[0].nombre)
         self.assertEquals('Taller de redes',evens[1].nombre)        
         self.assertEquals('Ponencia de ingenieria',evens[2].nombre)
         
