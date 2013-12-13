#!/usr/bin/env python
import sys
from heapq import heappush, heappop

class Grafo:
	def __init__(self):
		self.matriz = {}
		
	def agregar_vertice(self,v):
		"""
		Agrega un vertice al grafo
		"""
		self.matriz[v] = {}
		
	def agregar_arista(self,v1,v2,peso,nombre):
		"""
		Agrega una arista con nombre <nombre>, peso <peso>, que conecta <v1> y <v2>
		"""
		self.matriz[v1][v2] = (peso,nombre)
		self.matriz[v2][v1] = (peso,nombre) #grafo no dirigido!!
		
	def obtener_arista_peso(self,v1,v2):
		"""
		Obtiene el peso de la arista
		"""
		return self.matriz[v1][v2][0]

	def obtener_arista_id(self,v1,v2):
		"Obtiene el nombre de la arista"
		return self.matriz[v1][v2][1]	

	def borrar_arista(self,v1,v2):
		"""
		Elimina la arista que conecta <v1> con <v2>
		"""
		if self.hay_arista(v1,v2):
			del self.matriz[v1][v2]
			del self.matriz[v2][v1]
		
	def borrar_vertice(self,v):
		"""
		Elimina un vertice y sus aristas correspondientes
		"""
		for w in self.matriz.keys():
			if w.has_key(v):
				del w[v]
		del self.matriz[v]
	
	def hay_arista(self,v1,v2):
		"""
		Determina si dos vertices estan conectados.
		"""
		return v2 in self.matriz[v1]

	def adyacentes(self,v):
		"""
		Devuelve los adyacentes del vertice <v>.
		"""
		if self.pertenece(v):
			return self.matriz[v]
		else:
			print'Error: no hay adyacentes'

	def pertenece(self,v):
		"""
		Determina si un vertice esta en el grafo o no.
		"""
		return v in self.matriz.keys()
	
	def imprimir(self):
		"""
		Muestra la informacion del grafo
		"""
		for v in self.matriz.keys():
			print('{} : {}'.format(v, self.matriz[v]))

	def dijkstra(self, inicio):
		"""
		Obtiene el camino mas corto hacia todos los vertices del grafo, partiendo desde el vertice 			<inicio>.
		Devuelve una diccionario vertice:peso y otro con los predecesores de
		cada uno de los vertices"""
		infinito = sys.maxint
		# Inicializacion de estructuras auxiliares:
		#  pesos: diccionario vertice -> etiqueta
		#  disponibles: conjunto de vertices con etiquetas temporales
		#  hijos: diccionario vertice->predecesor para camino minimo)
		pesos = dict([(u, infinito) for u in self.matriz.keys()])
		pesos[inicio] = 0
		disponibles = []
		hijos = {}
		heappush(disponibles, (inicio, pesos[inicio]))
		# Ciclo principal
		while len(disponibles) != 0:
			next = heappop(disponibles)
			u = next[0] #obtengo el vertice de la tupla (vertice,peso)
			for v in self.adyacentes(u):
				if pesos[v] > pesos[u] + self.obtener_arista_peso(v,u):
					pesos[v] = pesos[u] + self.obtener_arista_peso(v,u)
					hijos[v] = u
					heappush(disponibles, (v, pesos[v]))
		return (pesos, hijos)

	def camino_minimo(self, inicio, fin):
		"""
		Devuelve el listado de vertices recorridos bajo el algoritmo de Dijkstra
		y el peso correspondiente al recorrido hecho en el grafo.
		"""
		camino = [str(fin)]
		if str(inicio) == str(fin):
			return camino, 0
		pesos, hijos = self.dijkstra(inicio)
		actual = fin
		while actual != inicio:
			camino.append(hijos[str(actual)])
			actual = hijos[str(actual)]
		return camino, pesos[str(fin)]

