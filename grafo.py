#!/usr/bin/env python
import heapq

class Grafo:
	def __init__(self):
		self.matriz = {}
		
	def agregar_vertice(self,v):
		self.matriz[v] = {}
		
	def agregar_arista(self,v1,v2,peso,nombre):
		self.matriz[v1][v2] = (peso,nombre)
		self.matriz[v2][v1] = (peso,nombre) #grafo no dirigido!!
		
	def obtener_arista_peso(self,v1,v2):
		return self.matriz[v1][v2][0]

	def obtener_arista_id(self,v1,v2):
		return self.matriz[v1][v2][1]	

	def borrar_arista(self,v1,v2):
		del self.matriz[v1][v2]
		del self.matriz[v2][v1]
		
	def borrar_vertice(self,v):
		for w in self.matriz.keys():
			if w.has_key(v):
				del w[v]
		del self.matriz[v]
	
	def hay_arista(self,v1,v2):
		if v2 in self.matriz[v1]:
			return True
		else:
			return False

	def adyacentes(self,v):
		return self.matriz[v]

	def dijkstra(self, inicio, fin):
    """
    Algoritmo de Dijkstra para el grafo G.
	Obtiene el camino más corto entre los vértices inicio y fin
    """
    infinito = 99999999999999 # Buscar un mejor criterio para infinito
    # Inicializacion de estructuras auxiliares:
    #  distancias: diccionario vertice -> etiqueta
    #  disponibles: conjunto de vertices con etiquetas temporales
    #  hijos: diccionario vertice->predecesor para camino minimo)
    distancias = dict([(u, infinito) for u in self.matriz.keys()])
    distancias[inicio] = 0
    disponibles = []
    hijos = {}
	heapq.heappush(disponibles, (inicio, distancias[inicio]))
    # Ciclo principal
    while next in disponibles:
        next = heapq.heappop(disponibles)
		u = next[0] #obtengo el vertice de la tupla (vertice,distancia)
        for v in self.adyacentes(u):
            if distancias[v] > distancias[u] + self.obtener_arista_peso(v,u):
                distancias[v] = distancias[u] + self.obtener_arista_peso(v,u)
                hijos[v] = u
				heapq.heappush(disponibles, (v, distancias[v]))
	return(distancias, hijos)



