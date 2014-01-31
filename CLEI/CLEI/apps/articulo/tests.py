from django.test import TestCase

from CLEI.apps.clei.clei import CLEI
from CLEI.apps.participante.models import Autor, MiembroComite
from .models import Articulo, Puntuacion, Topico

# Create your tests here.
class ArticuloTest(TestCase):
    def setUp(self):

    	# --------------------------------------------------------------------- 
    	# Creando topicos
    	# --------------------------------------------------------------------- 
    	t1 = Topico.objects.create(nombre_topico='Ingenieria')
    	t2 = Topico.objects.create(nombre_topico='Software')


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
        # Creando Articulos
        # --------------------------------------------------------------------- 
        articulo1 = Articulo.objects.create(id_articulo=1, titulo='Ingenieria de software', 
        								    resumen='Resumen',
        								    texto='Texto', p1='ingenieria', 
        								    p2='software')
        articulo1.autores = [autor1, autor2]

        articulo2 = Articulo.objects.create(id_articulo=2, titulo='Sistema de Informacion', 
        								    resumen='Resumen',
        								    texto='Texto', p1='sistema', p2='informacion', 
        								    p3='stakeholders')
        articulo2.autores = [autor1]


        # ---------------------------------------------------------------------
        # Creando los miembros del comite
        # ---------------------------------------------------------------------
        MiembroComite.objects.create(username='rmarquez', password='rmarquez', 
        							 correo='rmarquez@gmail.com', 
        							 es_presidente=True)

        MiembroComite.objects.create(username='jgonzalez', password='jgonzalez',
        							 correo='jgonzalez@gmail.com', 
        							 es_presidente=False)
        id1= MiembroComite.objects.all()[0].id
        id2= MiembroComite.objects.all()[1].id

		# ---------------------------------------------------------------------
        # Asignando las puntuaciones
        # ---------------------------------------------------------------------
        Puntuacion.objects.create(correo_id=id1, id_articulo_id=1, puntuacion=3.0)
        Puntuacion.objects.create(correo_id=id2, id_articulo_id=2, puntuacion=5.0)


    # Test de creacion de articulos
    def test_crear_articulos(self):
    	clei = CLEI()
    	clei.crear_articulos()

    	id1 = Articulo.objects.get(id_articulo=1).id_articulo
    	articulo1 = clei.get_articulos()[id1].id_articulo
    	id2 = Articulo.objects.get(id_articulo=2).id_articulo
    	articulo1 = clei.get_articulos()[id1].id_articulo
    	articulo2 = clei.get_articulos()[id2].id_articulo
    	self.assertEquals(articulo1, 1)
    	self.assertEquals(articulo2, 2)


    # Test de creacion de topicos
    def test_crear_topicos(self):
    	topicos = Topico.objects.all()
    	self.assertEquals('Ingenieria', topicos[0].nombre_topico)
    	self.assertEquals('Software', topicos[1].nombre_topico)


    # Test de cantidad de topicos registrados en la base de datos
    def test_num_topicos(self):
    	topicos = Topico.objects.all()
    	self.assertEquals(len(topicos), 2)


    # Test de asignacion de las puntuaciones a los articulos
    def test_puntuacion(self):
    	puntuaciones = Puntuacion.objects.all()
    	self.assertEquals(3.0, puntuaciones[0].puntuacion)
    	self.assertEquals(5.0, puntuaciones[1].puntuacion)