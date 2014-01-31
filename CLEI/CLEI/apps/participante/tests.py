from django.test import TestCase

from CLEI.apps.clei.clei import CLEI
from .models import Autor, MiembroComite, Inscrito

# Create your tests here.
class ParticipanteTest(TestCase):
    def setUp(self):

        inscrito1 = Inscrito.objects.create(username='daralion', password='daralion', 
                                                                  correo='daralion@gmail.com',nombre='Daralion', 
                                                                  apellido='Astrel',inst_afil='USB', url='', 
                                                                  telefono='04143124576')

        inscrito2 = Inscrito.objects.create(username='ruunna', password='ruunna', 
                                                                  correo='ruutel@gmail.com',nombre='Ruunna',
                                                                  apellido='Telien', inst_afil='USB', 
                                                                  telefono='04143124576')

        inscrito3 = Inscrito.objects.create(username='anna', password='tklde', 
                                                                  correo='alenner@gmail.com',nombre='Anna', 
                                                                  apellido='Lenner',  inst_afil='USB', 
                                                                  url='tka.com', telefono='02124563765')
   
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
            
    # Test de creacion de inscritos
    def test_crear_inscrito(self):
        inscritos = Inscrito.objects.all()

        self.assertEquals(len(inscritos), 3)

    def test_inscrito_campos_validos(self):
        inscritos = Inscrito.objects.all()

        self.assertEquals('daralion', inscritos[0].username)
        self.assertEquals('', inscritos[0].url)
        self.assertEquals('ruunna', inscritos[1].username)
        self.assertEquals(None,inscritos[1].url)
        self.assertEquals('anna', inscritos[2].username)
        self.assertEquals('tka.com', inscritos[2].url)