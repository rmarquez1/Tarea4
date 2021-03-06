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

    def get_articulos(self):
        return self.articulos

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
            elif articulos[i].aceptado_especial == True:
                id = articulos[i].id_articulo
                Articulo.objects.filter(id_articulo=id).update(aceptado_especial=False)
        
    # Metodo que limpia la lista de aceptables
    def limpiar_aceptables(self):
        self.aceptables = []
        
	
    # Metodo que limpia la lista de empatados
    def limpiar_empatados(self):
        self.empatados = []
        
    # Metodo que asigna false a los articulos que tienen el atributo falta 
    # cupo True
    def limpiar_falta_cupo(self):
	    articulos = Articulo.objects.filter(rechazado_falta_cupo = True)
	    for i in range(len(articulos)):
        	id = articulos[i].id_articulo
        	Articulo.objects.filter(id_articulo=id).update(rechazado_falta_cupo=False)
	
	# Metodo que devuelve una lista con las puntuaciones de un articulo dado
    def listar_puntuacion_por_articulo(self, id_articulo):
    	lista = []
    	puntuacion = Puntuacion.objects.all()
    	tam_puntuacion = len(puntuacion)
    	for i in range(tam_puntuacion):
    	    if id_articulo==puntuacion[i].id_articulo:
                lista.append(puntuacion[i].puntuacion)
    	return lista
  
    # Metodo que agrega las evaluaciones de los articulos
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
        if self.num_articulos + len(self.aceptados) > len(self.aceptables):
            return 0
        else:
            return self.num_articulos    

	# Metodo que almacena en una lista los articulos aceptados
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
	
    # Metodo que almacena en una lista los articulos empatados
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
            tam_lista_pais = len(lista_notas_por_pais)
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
                id = lista_minimos[i][1][j][0]
                self.set_aceptados(id)
                Articulo.objects.filter(id_articulo=id).update(aceptado=True)
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
        for i in range(tam_lista):
            promedios = self.listar_promedios(lista_no_aceptados[i][1])
            self.crear_aceptados_empatados(promedios, lista_no_aceptados[i][1])
            
	# -------------------------------------------------------------------------
    # MOSTRADO DE ESTADOS FINALES DE SELECCION
    # -------------------------------------------------------------------------
    
    # Metodo que retorna aquellos articulos cuyo estado final de seleccion 
    # es aceptado
    def mostrar_aceptados(self):
    	articulos = Articulo.objects.filter(aceptado=True)
    	return articulos
    
    # Metodo que retorna aquellos articulos cuyo estado final de seleccion 
    # es aceptado especial
    def mostrar_aceptados_especiales(self):
    	articulos = Articulo.objects.filter(aceptado_especial=True)
    	return articulos
    	
    # Metodo que retorna aquellos articulos cuyo estado final de seleccion 
    # es rechazado por promedios
    def mostrar_rechazados_promedio(self):
    	
    	articulos = Articulo.objects.filter(aceptado=False,
    										aceptado_especial=False,
    										rechazado_falta_cupo = False,
    										rechazado_por_promedio=False)
    	return articulos
    
    # Metodo que asigna True en el campo rechazado por falta de cupo a aquellos
    # articulos que listaron como empatados pero que no pudieron ser ingresados
    # a la lista de aceptados	
    def asignar_falta_cupo(self):
    	empatados = self.get_empatados()
    	tam = len(empatados)
    	for i in range(tam):
    		res = empatados[i] in self.aceptados
    		if res == False:
    			Articulo.objects.filter(id_articulo=empatados[i]).update(rechazado_falta_cupo=True)
    
    # Metodo que retorna aquellos articulos cuyo estado final de seleccion 
    # es rechazado por falta de cupo	
    def mostrar_falta_cupo(self):
    	articulos = Articulo.objects.filter(aceptado=False,
    										aceptado_especial=False,
    										rechazado_falta_cupo = True,
    										rechazado_por_promedio=False)
    	return articulos
    
    #------------------------------------------------------#
    # seleccion de articulos 80% por proporcion de paises  #
    #------------------------------------------------------#
    def seleccion_ochenta(self, numero):
        self.aceptables1 = []
        acept_aux = []
        acept = []
        cont_pais= {}
        acept_ochenta = []
        self.aceptables1 = self.aceptables[:]
        # se ordenan los paises por nota decendente
        self.aceptables1.sort(key= lambda x: x[1], reverse = True)
        # se genera una lista de articulos aceptables1 (objetos articulos)
        for i in self.aceptables1:
            acept.append(self.articulos[i[0]])
        num_articulos = len(acept)
        tam_aceptables = len(self.aceptables)
        for i in range(tam_aceptables):
        # Obtenemos la lista de los autores del articulo i
            autor = self.articulos[self.aceptables[i][0]].autores.all()
            # Obtenemos el pais del primer autor de la lista
            if cont_pais.has_key(autor[0].pais):
                cont_pais[autor[0].pais]= cont_pais[autor[0].pais] + 1
            else:
                cont_pais[autor[0].pais]= 1


        # se crea el iterador y para cada pais se recorre la lista de aceptados
        # seleccionando la cantidad correspondiente a ser admitida para ese pais
        acept_aux = acept[:]
        for j in cont_pais:
            k= 0
            m = ((0.8*numero/num_articulos)*cont_pais[j])-1
            m = round(m)

            for i in range(tam_aceptables):
             # Obtenemos la lista de los autores del articulo i
                autor = self.articulos[self.aceptables[i][0]].autores.all()
                # Obtenemos el pais del primer autor de la lista
                if j == autor[0].pais:
                    if k <= m:
                        acept_ochenta.append(acept.pop(acept.index(self.articulos[self.aceptables[i][0]])))
                        k = k + 1

        # se asigna a aceptables la lista de aceptables sin los que ya
        # han sido admitidos, esta lista contiene objetos Articulo, no tuplas
        self.aceptables1 = acept
        return acept_ochenta

    # Metodo que selecciona los 20% de la cantidad de articulos que se desea
    # admitir y los agrega a la lista de aceptados, si hay articulos en condicion
    # de empate los agrega a la lista de empatados
    def seleccion_veinte(self, numero):
        acept_veinte = []
        dic_prom= {}
        for i in self.aceptables:
            dic_prom[i[0]]=i[1]
        while numero > 0:
        #si n es menor al numero de articulos aceptables, debemos elegir cuales tomar
            if numero < len(self.aceptables1):
        # si el ultimo articulo no esta empatado con el siguiente, tomamos los n primeros
        # articulos de la lista de articulos aceptables
                a = self.aceptables1[numero-1].id_articulo
                b= self.aceptables1[numero].id_articulo
                if dic_prom[a] !=  dic_prom[b]:
                    acept_veinte = self.aceptables1[0:numero]
                    return acept_veinte
                #sino restamos uno, hasta encontrar un articulo que no este empatado con ninguno de
                # los que no hemos admitido
                else:
                    if numero > 0:
                        numero = numero - 1
            #si n es mayor o igual a numero de articulos aceptables
            else:
        # admitidos sera igual a aceptables
                acept_veinte = self.aceptables1
                return acept_veinte

        return acept_veinte

    def empatados_veinte(self, numero):
        empat = []
        acept= self.seleccion_veinte(numero)
        dic_prom= {}
        for i in self.aceptables:
            dic_prom[i[0]]=i[1]
        if len(acept) != numero:
            no_admitidos= self.aceptables1[len(acept):len(self.aceptables1)]
            if len(acept) < len(self.aceptables1):
                indice = dic_prom[self.aceptables1[len(acept)].id_articulo]
                for i in no_admitidos:
                    if dic_prom[i.id_articulo] == indice:
                        empat.append(i)
        return[acept, empat]

     # selecciona el 80% de la cantidad de articulos a filtrar segun su pais
    # el otro 20% lo selecciona por indice
    # en caso de haber casos de empate que no quepan en la lista de admitidos
    # se almacenan en la lista de empatados para el desempate por parte del
    # presidente
    def seleccion_equitativa(self, numero):
        self.aceptados = []
        self.empatados = []
        self.agregar_evaluaciones()
        acept = self.seleccion_ochenta(numero)
        resto = self.empatados_veinte(numero - len(acept))
        acept_veinte = resto[0]
        empat = resto[1]
        for i in acept:
            self.set_aceptados(i.id_articulo)
            Articulo.objects.filter(id_articulo=i.id_articulo).update(aceptado=True)
        for i in acept_veinte:
            self.set_aceptados(i.id_articulo)
            Articulo.objects.filter(id_articulo=i.id_articulo).update(aceptado=True)
        for i in empat:
            self.set_empatados(i.id_articulo)
            Articulo.objects.filter(id_articulo=i.id_articulo).update(rechazado_falta_cupo = True)
        if numero > len(self.aceptables):
            return 0
        else:
            return numero - len(self.aceptados)


    # Metodo para seleccionar la cantidad de articulos a aceptar
    # manteniendo la proporcion entre topicos diferentes
    #
    def seleccion_topicos(self, numero):
        self.aceptados = []
        self.empatados = []
        acept_aux = []
        acept = []
        cont_topico= {}
        acept_topicos = []
        self.aceptables1 = self.aceptables[:]
        # se ordenan los paises por nota decendente
        self.aceptables1.sort(key= lambda x: x[1], reverse = True)
        # se genera una lista de articulos aceptables1 (objetos articulos)
        for i in self.aceptables1:
            acept.append(self.articulos[i[0]])
        num_articulos = len(acept)



        # se cuentan cuantos articulos hay de cada pais
        # y se almacena en un diccionario
        for i in acept:
            if cont_topico.has_key(i.topicos.all()[0].nombre_topico):
                cont_topico[i.topicos.all()[0].nombre_topico]= cont_topico[i.topicos.all()[0].nombre_topico] + 1
            else:
                cont_topico[i.topicos.all()[0].nombre_topico]= 1
        # se crea el iterador y para cada pais se recorre la lista de aceptados
        # seleccionando la cantidad correspondiente a ser admitida para ese pais
        acept_aux = acept[:]
        for j in cont_topico:
            k= 0
            m = ((1.0*numero/num_articulos)*cont_topico[j])-1
            for i in acept_aux:
                    if j == i.topicos.all()[0].nombre_topico:
                        if k <= m:
                            acept_topicos.append(acept.pop(acept.index(i)))
                            k = k + 1

        # se asigna a aceptables la lista de aceptables sin los que ya
        # han sido admitidos, esta lista contiene objetos Articulo, no tuplas
        for i in acept_topicos:
            self.set_aceptados(i.id_articulo)
            Articulo.objects.filter(id_articulo=i.id_articulo).update(aceptado=True)
        return 0


    # Estrategia 3 (segun documento) del requisito de seleccion de articulos
    def aceptar_por_notas_corte(self, n1, n2):
        aceptados     = []
        participacion = {}
        pendientes    = {}
        capacidad     = self.num_articulos
        articulos     = sorted(self.aceptables, key=(lambda x : x[1]), reverse=True)

        if n2 >= n1:
            raise ValueError

        for articulo in articulos:
            id_articulo = articulo[0]
            promedio    = articulo[1]
            pais        = self.articulos[id_articulo].get_pais()

            if len(aceptados) == capacidad:
                self.aceptados = aceptados
                return

            if not pais in participacion:
                participacion[pais] = 0
                pendientes[pais]    = []

            if promedio >= n1:
                aceptados.append(id_articulo)
                self.articulos[id_articulo].set_aceptado(True)
                participacion[pais] += 1

            elif promedio >= n2:
                pendientes[pais].append(id_articulo)

            else:
                break

        prioridad = sorted(participacion.keys(), key=(lambda x : participacion[x]))

        for pais in prioridad:

            while pendientes[pais] and capacidad > len(aceptados):
                id_articulo = pendientes[pais].pop(0)
                aceptados.append(id_articulo)
                self.articulos[id_articulo].set_aceptado(True)

        self.aceptados = aceptados

