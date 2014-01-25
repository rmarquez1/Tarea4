from django import forms

from CLEI.apps.articulo.models import Articulo, Topico, Puntuacion
from CLEI.apps.participante.models import Autor, MiembroComite
from .models import Clei

# Create your models here.
class CLEI():
    def __init__(self):
        self.num_articulos = 0
        self.aceptables = []
        self.aceptables1 = []
        self.aceptados = []
        self.empatados = []
        self.articulos = {}
        self.lista_articulos = []
        self.miembros_cp = {}
        self.evaluaciones = {}
        self.inscritos = {}
        
    def get_num_articulos(self):
	   return self.num_articulos

    # Metodo que retorna la lista de aceptables
    def get_aceptables(self):
        return self.aceptables

    # Metodo que retorna la lista de aceptados
    def get_aceptados(self):
        return self.aceptados
        
    # Metodo que devuelve la lista de empatados
    def get_empatados(self):
        return self.empatados
        
    # Asigna la cantidad de articulos al congreso
    def set_num_articulos(self, num_articulos):
	   self.num_articulos = num_articulos
	
    # Metodo que inserta una tupla (idArticulo, promedio) en la lista de los 
    # aceptables
    def set_aceptables(self, id_articulo, promedio):
        t = (id_articulo, promedio)
        self.aceptables.append(t)

    # Metodo que inserta el id de articulo en la lista de aceptados
    def set_aceptados(self, id_articulo):
        self.aceptados.append(id_articulo)

    # Metodo que inserta el id de articulo en la lista de empatados
    def set_empatados(self, id_articulo):
        self.empatados.append(id_articulo)
        
    # Metodo que crea el diccionario de articulos
    def crear_articulos(self):
    	a = Articulo.objects.all()
    	tam_articulos = len(a)
    	for i in range(tam_articulos):
    	    self.articulos[a[i].id_articulo] = a[i]
    # Metodo que limpia la lista de aceptados y asigna false a todos los 
    # articulos que tenga True en el atributo de aceptado
    def limpiar_aceptados(self):
        self.aceptados = []
        articulos = Articulo.objects.all()
        for i in range(len(articulos)):
            if articulos[i].aceptado == True:
                id = articulos[i].id_articulo
                Articulo.objects.filter(id_articulo=id).update(aceptado=False)
        
    # Metodo que limpia la lista de aceptables
    def limpiar_aceptables(self):
        self.aceptables = []
	
    # Metodo que limpia la lista de empatados
    def limpiar_empatados(self):
        self.empatados = []
	
	# Metodo que devuelve una lista con las puntuaciones de un articulo dado
    def listar_puntuacion_por_articulo(self, id_articulo):
    	lista = []
    	puntuacion = Puntuacion.objects.all()
    	tam_puntuacion = len(puntuacion)
    	for i in range(tam_puntuacion):
    	    if id_articulo==puntuacion[i].id_articulo:
                lista.append(puntuacion[i].puntuacion)
    	return lista
  
    def agregar_evaluaciones(self):
        promedio = 0
        articulos = Articulo.objects.all()
        puntuacion = Puntuacion.objects.all()
        tam_articulos = len(articulos)
        tam_puntuacion = len(puntuacion)
        for i in range(tam_articulos):
            suma = 0
            k = 0
            lista = self.listar_puntuacion_por_articulo(articulos[i])
            tam = len(lista)
            if tam != 0:
                for j in range(tam):
                    suma += lista[j]
                promedio = float(suma) / tam
            self.evaluaciones[articulos[i].id_articulo] = promedio
	
	
    # -------------------------------------------------------------------------
    # SELECCION POR DESEMPATE
    # -------------------------------------------------------------------------
    
    # Metodo que agrega a la lista aquellos articulos que son considerados
    # como aceptables
    def crear_aceptables(self):
    	self.agregar_evaluaciones()
    	if len(self.evaluaciones) != 0:
    	    lista_evaluaciones = self.evaluaciones.items()
    	    lista_evaluaciones.sort(key=lambda x:x[1])
    	    lista_evaluaciones.reverse()
    	    tam_evaluaciones= len(lista_evaluaciones)
    	    for i in range(tam_evaluaciones):
        		if Puntuacion.objects.filter(id_articulo=lista_evaluaciones[i][0]).count()>=2:
        		    if lista_evaluaciones[i][1]>=3.0:
            			self.set_aceptables(lista_evaluaciones[i][0],
            					    lista_evaluaciones[i][1])
    	return self.aceptables
	
    # Retorna una lista con los promedios de articulos en una lista dada
    def listar_promedios(self, lista):
        promedios = []
        tam = len(lista)
        # Ciclo que inserta en la lista promedios solo los promedios de los 
        # articulos aceptables
        for i in range(tam):
            promedios.append(lista[i][1])
        return promedios	

    # Metodo que crea las listas de empatados y aceptados
    def crear_aceptados_empatados(self, promedios, lista):
        tam = len(promedios)
        i = 0
        j = 0
        
        # Ciclo que recorre la lista de promedios y cuenta las veces en que 
        # aparece un promedio para insertarlo en la lista de aceptados o
        # empatados
        while i<tam:
            # Se cuenta las veces en que aparece el valor de promedios[i]
            contar = promedios.count(promedios[i])
            
            # Llenando lista de ACEPTADOS
            # Si contar es menor a la cantidad de articulos que deben ser
            # aceptados en el congreso, insertamos los articulos correspondientes
            # a ese promedio en la lista de aceptados
            if contar <= self.num_articulos:
                j = i
                # variable que cuenta las veces que debe ingresar un elemento a
                # la lista de acuerdo a la variable contar
                temp = 0
                while j < tam:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Asignamos True al articulo para indicar que fue 
                        # aceptado
                        
                        # Agregamos el id del articulo a la lista de aceptados
                        id_articulo = lista[j][0]
                        self.set_aceptados(id_articulo)
                        Articulo.objects.filter(id_articulo=id_articulo).update(aceptado=True)
                        
                        # Asignamos True al atributo aceptado del articulo
                        #self.articulos[id_articulo].set_aceptado(True)
                        
                        j = j + 1
                        # Sumamos uno a la variable temporal
                        temp = temp + 1
                        
                    else: # Caso en que ya se han agregado los articulos
                        break
                # Reduzco el numero de articulos a ser aceptados     
                self.num_articulos -= contar
                # Posicionamos i en i + contar del arreglo 
                i = i + contar
            
            else: # Llenando la lista de EMPATADOS
                j = i
                # variable que cuenta las veces que debe ingresar un elemento a
                # la lista de acuerdo a la variable contar
                temp = 0
                while j < tam:
                    
                    # Caso en que aun no se han agregado la cantidad de articulos
                    # indicados por la variable contar
                    if temp != contar:
                        # Agregamos a la lista de empatados
                        self.set_empatados(lista[j][0])
                        j = j + 1
                        # Sumamos uno a la variable temporal
                        temp = temp + 1
                    else: # Caso en que ya se han agregado los articulos
                        break
                break
        # Retorna el numero de espacios restantes en la lista de aceptados       
        return self.num_articulos     

    def guardar_aceptados(self):
    	lista = []
    	for i in range(len(self.get_aceptados())):
    	    lista.append(Articulo.objects.filter(id_articulo=self.get_aceptados()[i]))
    	articulos = []
    	for i in range(len(lista)):
    	    res = lista[i][0] in articulos
    	    if res == False:
    		  articulos.append(lista[i][0])
    	return articulos
	
    def guardar_empatados(self):
    	lista = []
    	for i in range(len(self.get_empatados())):
    	    lista.append(Articulo.objects.filter(id_articulo=self.get_empatados()[i]))
    	articulos = []
    	for i in range(len(lista)):
            res = lista[i][0] in articulos
            if res == False:
              articulos.append(lista[i][0])
    	return articulos
	
    # Esquema de seleccion por desempate
    def seleccionar_desempate(self, id):
        if id in self.get_empatados():
            self.set_aceptados(id)
            
    # -------------------------------------------------------------------------
    # SELECCION POR PAIS
    # -------------------------------------------------------------------------
    
    # Retorna una lista con los ids de los articulos pertenecientes a la lista
    # de aceptables
    def listar_id_aceptables(self):
        lista_id_articulos = []
        # Ciclo que agrega a la lista de articulos los ids de los articulos
        # pertenecientes a la lista de aceptables
        for i in range(len(self.aceptables)):
            lista_id_articulos.append(self.aceptables[i][0])
        return lista_id_articulos
        
        
    # Generamos una lista con todos los paises del congreso que enviaron sus
    # articulos al congreso
    def paises_conferencia(self):
        lista_paises = []
	
        lista_id_articulos = self.listar_id_aceptables() 
        tam_articulos = len(lista_id_articulos)
        # Ciclo que recorre la lista de articulos aceptables con cada id y 
        # asigna el pais de los articulos que estan de primero en la lista de 
        # autores de cada articulo
        for i in range(tam_articulos):
            # Obtenemos la lista de los autores del articulo i
            autor = self.articulos[lista_id_articulos[i]].autores.all()
            # Obtenemos el pais del primer autor de la lista
            pais = autor[0].pais
            # Si no esta el pais en la lista de articulos
            esta_pais = pais in lista_paises
            if  esta_pais == False:
                lista_paises.append(pais)
                
        return lista_paises
        
    # Retorna una lista con las notas de los articulos presentados por un pais
    # dado y que pertenece a la lista de aceptables
    def listar_notas_por_pais(self, pais):
        lista_notas = []
        tam_aceptables = len(self.aceptables)
        # Ciclo que verifica que el pais de cada articulo sea igual al dado 
        # y este es insertado en la lista
        for i in range(tam_aceptables):
	    # Obtenemos la lista de los autores del articulo i
            autor = self.articulos[self.aceptables[i][0]].autores.all()
            # Obtenemos el pais del primer autor de la lista
            pais1 = autor[0].pais
            if  pais1 == pais:
                lista_notas.append(self.aceptables[i])
        # Ordenamos de mayor a menor por nota
        lista_notas.sort(key=lambda x:x[1], reverse = True)
        return lista_notas
        
    # Retorna una lista cuyos elementos son tuplas (pais, [lista de notas])
    def listar_articulos_por_pais(self, num_articulos_por_pais):
        # Creamos una lista que contendra tuplas ('Pais', [articulos])
        lista_paises = []
        # Generemos lista de los paises cuyos articulos son aceptables
        lista = self.paises_conferencia()
        tam_lista = len(lista)
        for i in range(tam_lista):
            # Obtenemos una lista con los articulos del pais en la posicion i
            lista_notas_por_pais = self.listar_notas_por_pais(lista[i])
            #print 'pais: ', lista[i], ' lista notas: ', lista_notas_por_pais
            tam_lista_pais = len(lista_notas_por_pais)
            #print tam_lista_pais
            # Si la cantidad de articulos del pais es mayor o igual al minimo 
            # de articulos por pais
            if tam_lista_pais >= num_articulos_por_pais:
                l = []
                for j in range(tam_lista_pais):
                    l.append(lista_notas_por_pais[j])
                # Creamos una tupla ('Pais', [articulos])
                t = (lista[i], l)
                # Agregas a la lista paises
                lista_paises.append(t)
            # Ordenamos la lista de menor a mayor dependiendo de la cantidad de
            # articulos aceptables por pais
            lista_paises.sort(key=lambda x:len(x[1]))
        return lista_paises
    
    # Retorna una lista con las tuplas (pais, [lista de notas]) donde esa lista
    # de notas contiene la cantidad minima de articulos
    def cantidad_min_articulos(self, num_articulos_por_pais):
        lista_min = []
        lista_paises = self.listar_articulos_por_pais(num_articulos_por_pais)
        tam_lista_paises = len(lista_paises)
        
        for i in range(tam_lista_paises):
            # Tamanio de la lista de notas de cada pais
            tam = len(lista_paises[i][1])
            j = 0
            # Creamos una lista que contendra los articulos (notas)
            l = []
            # Ciclo que agrega en una lista el numero minimo de articulos por 
            # pais
            while j < num_articulos_por_pais:
                l.append(lista_paises[i][1][j])
                #del lista_paises[i][1][j]
                j += 1
                # Eliminamos la nota que agregamos a la lista
                
            t = (lista_paises[i][0], l)
            lista_min.append(t)
        #print 'Lista_ PAISES: ', lista_paises
        return lista_min

    # Tipo de seleccion por pais
    def agregar_aceptados(self, num_articulos_por_pais):
        lista_minimos = self.cantidad_min_articulos(num_articulos_por_pais)
        tam_minimos = len(lista_minimos)
        for i in range(tam_minimos):
            tam = len(lista_minimos[i][1])
            j = 0
            while j < tam:
                # Insertamos a la lista de aceptados
                self.set_aceptados(lista_minimos[i][1][j][0])
                self.num_articulos -= 1 
                j += 1
        return self.num_articulos
            
    # Metodo que genera una lista de aquellos articulos que no estan en la lista
    # de aceptados
    def listar_no_aceptados(self,num_articulos_por_pais):
        # Generamos una lista donde estaran los articulos que aun no han
        # sido aceptados
        lista_por_seleccionar = []
        lista_articulos = self.listar_articulos_por_pais(num_articulos_por_pais)
        tam_paises = len(lista_articulos)
        for i in range(tam_paises):
            # Generamos una lista con los articulos representados del pais i
            lista = self.listar_notas_por_pais(lista_articulos[i][0])
            #print 'lista articulos: '
            #print lista
            l = []
            tam = len(lista)
            # Ciclo que construye una lista con aquellos paises y sus articulos
            # que aun no pertenecen a la lista aceptados. Esto para manejar
            # la escogencia de articulos cuando el numero de articulos es mayor
            # que la cantidad de articulos aceptados por el momento
            for j in range(tam):
                
                res = lista[j][0] in self.aceptados
                # Caso en que el id del articulo no pertenezca a los aceptados
                if res == False:
                    l.append(lista[j])
            # Caso en que se consiguio articulos que no han sido aceptados
            if len(l) != 0:
                t = (lista_articulos[i][0], l)
                lista_por_seleccionar.append(t)
                    
        return lista_por_seleccionar
        
    # Metodo que selecciona los articulos restantes para completar la capacidad
    # maximo de articulos escogidos en la conferencia
    def seleccionar_por_pais(self, num_articulos_por_pais):
        lista_no_aceptados = self.listar_no_aceptados(num_articulos_por_pais)
        tam_lista = len(lista_no_aceptados)
        print 'lista no aceptados: ', lista_no_aceptados
        for i in range(tam_lista):
            promedios = self.listar_promedios(lista_no_aceptados[i][1])
            self.crear_aceptados_empatados(promedios, lista_no_aceptados[i][1])