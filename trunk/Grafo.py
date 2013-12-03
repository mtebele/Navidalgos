#!/usr/bin/env python

class Grafo:
	def __init__(self):
		self.matriz = {}
		
	def agregar_vertice(self,v):
		self.matriz[v] = {}
		
	def agregar_arista(self,v1,v2,peso):
		self.matriz[v1][v2] = peso
		self.matriz[v2][v1] = peso #grafo no dirigido!!
		
	def obtener_arista(self,v1,v2):
		return self.matriz[v1][v2]
		
	def borrar_arista(self,v1,v2):
		self.matriz[v1][v2] = 0
		self.matriz[v2][v1] = 0
		
	def borrar_vertice(self,v)
		for w in self.matriz.keys()
			if w.has_key(v)
				del w[v]
		del self.matriz[v]
		
	def hay_arista(self,v1,v2):
		return self.matriz[v1][v2] != 0
	