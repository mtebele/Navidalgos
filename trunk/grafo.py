#!/usr/bin/env python
import sys
from heapq import heappush, heappop

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
		return v2 in self.matriz[v1]

	def adyacentes(self,v):
		if v in self.matriz.keys():
			return self.matriz[v]
		else:
			return {}

	def dijkstra(self, inicio, fin):
		"""Obtiene el camino mas corto entre los vertices inicio y fin"""
		infinito = sys.maxint
		# Inicializacion de estructuras auxiliares:
		#  distancias: diccionario vertice -> etiqueta
		#  disponibles: conjunto de vertices con etiquetas temporales
		#  hijos: diccionario vertice->predecesor para camino minimo)
		distancias = dict([(u, infinito) for u in self.matriz.keys()])
		distancias[inicio] = 0
		disponibles = []
		hijos = {}
		heappush(disponibles, (inicio, distancias[inicio]))
		# Ciclo principal
		while len(disponibles) != 0:
			next = heappop(disponibles)
			u = next[0] #obtengo el vertice de la tupla (vertice,distancia)
			for v in self.adyacentes(u):
				if distancias[v] > distancias[u] + self.obtener_arista_peso(v,u):
					distancias[v] = distancias[u] + self.obtener_arista_peso(v,u)
					hijos[v] = u
					heappush(disponibles, (v, distancias[v]))
		return(distancias, hijos)



