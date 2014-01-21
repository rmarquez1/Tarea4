from django import forms

from CLEI.apps.articulo.models import Articulo, Topico, Puntuacion

# Create your models here.
class Clei():
    def __init__(self, num_articulos=None):
	self.num_articulos = num_articulos
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
	articulos = Articulo.objects.all()
	tam_articulos = len(articulos)
	for i in range(tam_articulos):
	    self.articulos[articulos.id_articulo] = articulos[i]
  
    def listar_puntuacion_por_articulo(self, id_articulo):
	lista = []
	puntuacion = Puntuacion.objects.all()
	tam_puntuacion = len(puntuacion)
	for i in range(tam_puntuacion):
	    if id_articulo==puntuacion[i].id_articulo:
		lista.append(puntuacion[i].puntuacion)
	return lista
  
    def get_evaluaciones(self):
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
	    
    def crear_aceptables(self):
	self.get_evaluaciones()
	print self.evaluaciones
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
	    articulos.append(lista[i][0])
	return articulos
	
    def guardar_empatados(self):
	lista = []
	for i in range(len(self.get_empatados())):
	    lista.append(Articulo.objects.filter(id_articulo=self.get_empatados()[i]))
	articulos = []
	for i in range(len(lista)):
	    articulos.append(lista[i][0])
	return articulos