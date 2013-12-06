#!/usr/bin/env python

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

