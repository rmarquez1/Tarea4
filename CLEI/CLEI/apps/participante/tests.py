from django.test import TestCase

from CLEI.apps.clei.clei import CLEI
from .models import Autor, MiembroComite

# Create your tests here.
class ParticipanteTest(TestCase):
    def setUp(self):


    	# --------------------------------------------------------------------- 
    	# Creando autores
    	# --------------------------------------------------------------------- 
    	autor1 = Autor.objects.create(username='lgonzalez', password='lgonzalez', 
    								  correo='lgonzalez@gmail.com',
    								  nombre='Lestsael', apellido='Gonzalez', 
    								  inst_afil='USB', pais='Venezuela')
        
    	autor2 = Autor.objects.create(username='gmartinez', password='gmartinez', 
    								  correo='gmartinez@gmail.com',
    								  nombre='Gabriel', apellido='Martinez', 
    								  inst_afil='USB', pais='Venezuela')

        # ---------------------------------------------------------------------
        # Creando los miembros del comite
        # ---------------------------------------------------------------------
        MiembroComite.objects.create(username='rmarquez', password='rmarquez', 
        							 correo='rmarquez@gmail.com', 
        							 nombre = 'Ramon', apellido='Marquez',
        							 inst_afil='USB',es_presidente=True)

        MiembroComite.objects.create(username='jgonzalez', password='jgonzalez',
        							 correo='jgonzalez@gmail.com', 
        							 nombre = 'Jesus', apellido='Gonzalez',
        							 inst_afil='UCV',es_presidente=False)

        id1= MiembroComite.objects.all()[0].id
        id2= MiembroComite.objects.all()[1].id


    # Test de creacion de autores
    def test_crear_autor(self):
    	autores = Autor.objects.all()

    	self.assertEquals('lgonzalez', autores[0].username)
    	self.assertEquals('gmartinez', autores[1].username)
    	self.assertEquals('Lestsael', autores[0].nombre)
    	self.assertEquals('Gabriel', autores[1].nombre)


	# Test de creacion de miembros de comite
    def test_crear_miembro_comite(self):
    	miembros = MiembroComite.objects.all()

    	self.assertEquals('rmarquez', miembros[0].username)
    	self.assertEquals('jgonzalez', miembros[1].username)
    	self.assertEquals('Ramon', miembros[0].nombre)
    	self.assertEquals('Jesus', miembros[1].nombre)


    # Test de cantidad de autores registrados
    def test_num_autores(self):
    	autores = Autor.objects.all()

    	self.assertEquals(len(autores),2)


    # Test de cantidad de topicos registrados
    def test_num_miembros_comite(self):
    	miembros = MiembroComite.objects.all()

    	self.assertEquals(len(miembros),2)