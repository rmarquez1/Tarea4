from django.test import TestCase

from CLEI.apps.clei.clei import CLEI
from CLEI.apps.participante.models import Autor, MiembroComite
from CLEI.apps.articulo.models import Articulo, Puntuacion

# Create your tests here.
class CleiTest(TestCase):
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

        autor3 = Autor.objects.create(username='rmartinez', password='rmartinez', 
                                      correo='rmartinez@gmail.com',
                                      nombre='Raquel', apellido='Marquez', 
                                      inst_afil='UCV', pais='Canada')

        autor4 = Autor.objects.create(username='jortiz', password='jortiz', 
                                      correo='jortiz@gmail.com',
                                      nombre='Jose', apellido='Ortiz', 
                                      inst_afil='UCV', pais='Canada')

        autor5 = Autor.objects.create(username='cgarce', password='cgarce', 
                                      correo='cgarce@gmail.com',
                                      nombre='Carla', apellido='Garce', 
                                      inst_afil='USB', pais='Brasil')

        autor6 = Autor.objects.create(username='cbarazarte', password='cbarazarte', 
                                      correo='cbarazarte@gmail.com',
                                      nombre='Carla', apellido='Barazarte', 
                                      inst_afil='USB', pais='Italia')

        # --------------------------------------------------------------------- 
        # Creando Articulos
        # --------------------------------------------------------------------- 
        articulo1 = Articulo.objects.create(id_articulo=1, titulo='Ingenieria de software', 
                                            resumen='Resumen', aceptado=False,
                                            aceptado_especial=False, 
                                            rechazado_falta_cupo=False,
                                            rechazado_por_promedio=False,
                                            texto='Texto', p1='ingenieria', 
                                            p2='software')
        articulo1.autores = [autor1]


        articulo2 = Articulo.objects.create(id_articulo=2, titulo='Sistema de Informacion', 
                                            resumen='Resumen', aceptado=False,
                                            aceptado_especial=False, 
                                            rechazado_falta_cupo=False,
                                            rechazado_por_promedio=False,
                                            texto='Texto', p1='sistema', 
                                            p2='informacion', p3='stakeholders')
        articulo2.autores = [autor2]


        articulo3 = Articulo.objects.create(id_articulo=3, titulo='Software', 
                                            resumen='Resumen', aceptado=False,
                                            aceptado_especial=False, 
                                            rechazado_falta_cupo=False,
                                            rechazado_por_promedio=False, 
                                            texto='Texto', p1='')
        articulo3.autores = [autor3]



        articulo4 = Articulo.objects.create(id_articulo=4, titulo='Embarazo', 
                                            resumen='Resumen', aceptado=False,
                                            aceptado_especial=False, 
                                            rechazado_falta_cupo=False,
                                            rechazado_por_promedio=False,
                                            texto='Texto', 
                                            p1='embarazo', p2='mujer')
        articulo4.autores = [autor4]



        articulo5 = Articulo.objects.create(id_articulo=5, titulo='Lenguaje de programacion', 
                                            resumen='Resumen', aceptado=False,
                                            aceptado_especial=False, 
                                            rechazado_falta_cupo=False,
                                            rechazado_por_promedio=False, texto='Texto', 
                                            p1='lenguaje', p2='programacion')
        articulo5.autores = [autor5]


        articulo6 = Articulo.objects.create(id_articulo=6, titulo='Base de datos', 
                                            resumen='Resumen', aceptado=False,
                                            aceptado_especial=False, 
                                            rechazado_falta_cupo=False,
                                            rechazado_por_promedio=False,
                                            texto='Texto', p1='base de datos')

        articulo6.autores= [autor1]



        articulo7 = Articulo.objects.create(id_articulo=7, 
                                            titulo='Software Libre vs Software Propietario', 
                                            resumen='Resumen', aceptado=False,
                                            aceptado_especial=False, 
                                            rechazado_falta_cupo=False,
                                            rechazado_por_promedio=False,
                                            texto='Texto', 
                                            p1='software libre', 
                                            p2='software propietario')
        articulo7.autores = [autor6]


        # ---------------------------------------------------------------------
        # Creando los miembros del comite
        # ---------------------------------------------------------------------
        MiembroComite.objects.create(username='rmarquez', password='rmarquez', 
                                     correo='rmarquez@gmail.com', 
                                     es_presidente=True)

        MiembroComite.objects.create(username='jgonzalez', password='jgonzalez',
                                     correo='jgonzalez@gmail.com', 
                                     es_presidente=False)

        MiembroComite.objects.create(username='fcolina', password='fcolina',
                                     correo='fcolina@gmail.com', 
                                     es_presidente=False)

        MiembroComite.objects.create(username='ireveron', password='ireveron',
                                     correo='ireveron@gmail.com', 
                                     es_presidente=False)

        id1= MiembroComite.objects.all()[0].id
        id2= MiembroComite.objects.all()[1].id
        id3= MiembroComite.objects.all()[2].id
        id4= MiembroComite.objects.all()[3].id

        # ---------------------------------------------------------------------
        # Asignando las puntuaciones
        # ---------------------------------------------------------------------
        Puntuacion.objects.create(correo_id=id1, id_articulo_id=1, puntuacion=3.0)
        Puntuacion.objects.create(correo_id=id1, id_articulo_id=2, puntuacion=4.0)
        Puntuacion.objects.create(correo_id=id2, id_articulo_id=2, puntuacion=5.0)
        Puntuacion.objects.create(correo_id=id3, id_articulo_id=3, puntuacion=4.5)
        Puntuacion.objects.create(correo_id=id2, id_articulo_id=3, puntuacion=3.5)
        Puntuacion.objects.create(correo_id=id4, id_articulo_id=4, puntuacion=2.5)
        Puntuacion.objects.create(correo_id=id3, id_articulo_id=5, puntuacion=3.5)
        Puntuacion.objects.create(correo_id=id4, id_articulo_id=2, puntuacion=3.0)
        Puntuacion.objects.create(correo_id=id1, id_articulo_id=7, puntuacion=4.5)
        Puntuacion.objects.create(correo_id=id3, id_articulo_id=7, puntuacion=4.0)
        Puntuacion.objects.create(correo_id=id2, id_articulo_id=1, puntuacion=5.0)
        Puntuacion.objects.create(correo_id=id2, id_articulo_id=4, puntuacion=4.5)



    # Test de listar los paises participantes en la conferencia
    def test_paises_conferencia(self):
        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()

        lista_paises = clei.paises_conferencia()
        self.assertEquals('Italia', lista_paises[0])


    # Test que lista los articulos de cada pais
    def test_listar_articulos_pais(self):
        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()

        lista_paises = clei.listar_articulos_por_pais(2)
        self.assertEquals(len(lista_paises[0][1]), 2)


    # Test de cantidad minima de articulos
    def test_cantidad_min_articulos(self):
        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()

        lista_min = clei.cantidad_min_articulos(2)
        self.assertEquals(len(lista_min[0][1]), 2)
        self.assertEquals(len(lista_min[1][1]), 2)


    # Test de agregar los aceptados
    def test_agregar_aceptados(self):
        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()

        clei.set_num_articulos(4)
        num_articulos = clei.agregar_aceptados(2)
        self.assertEquals(0, num_articulos)


        clei.set_num_articulos(5)
        num_articulos = clei.agregar_aceptados(2)
        self.assertEquals(1, num_articulos)


    # Test de seleccion por desempate
    def test_seleccion_desempate(self):
        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()

        clei.set_num_articulos(2)
        promedios = clei.listar_promedios(clei.get_aceptables())
        limite = clei.crear_aceptados_empatados(promedios, clei.get_aceptables())
        self.assertEquals(7, clei.get_aceptados()[0])
        self.assertEquals(3, clei.get_empatados()[0])


        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()
        clei.set_num_articulos(4)
        promedios = clei.listar_promedios(clei.get_aceptables())
        limite = clei.crear_aceptados_empatados(promedios, clei.get_aceptables())
        self.assertEquals(7, clei.get_aceptados()[0])
        self.assertEquals(1, len(clei.get_empatados()))


    # Test de seleccion por pais
    def test_seleccion_pais(self):
        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()

        clei.set_num_articulos(4)
        num_articulos = clei.agregar_aceptados(2)
        clei.seleccionar_por_pais(2)
        self.assertEquals(0, clei.get_num_articulos())

        clei.set_num_articulos(5)
        num_articulos = clei.agregar_aceptados(2)
        clei.seleccionar_por_pais(2)
        self.assertEquals(1, clei.get_num_articulos())


    # Test de estados de seleccion
    def test_estados_seleccion(self):
        clei = CLEI()
        clei.crear_articulos()
        clei.crear_aceptables()
        clei.set_num_articulos(4)
        promedios = clei.listar_promedios(clei.get_aceptables())
        limite = clei.crear_aceptados_empatados(promedios, clei.get_aceptables())
        articulo = Articulo.objects.filter(aceptado=True)
        self.assertTrue(articulo[0].aceptado, "El articulo debe ser aceptado")
        