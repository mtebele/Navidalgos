import grafo
import math
import numpy as np
from grafo import Grafo

class Ciudad:
	def __init__(self):
		self.mapa = Grafo()
		self.coord_angulares = {}
		self.coord_metros = {}

	def obtener_mapa(self):
		return self.mapa

	def calcular_distancia(self, esquina1, esquina2):
		"""
		Calcula la distancia entre las esquinas
		<esquina1> y <esquina2>	pertenecientes a la ciudad.
		"""
		coord_metros_1 = self.coord_metros[esquina1]
		coord_metros_2 = self.coord_metros[esquina2]
		dist = coord_metros_2 - coord_metros_1
		return math.hypot(dist[0], dist[1])

	def agregar_esquina(self, esquina, x, y, lat, lon):
		"""
		Agrega la esquina <esquina> con las coordenadas
		(x,y), (lat, lon)
		"""		
		self.mapa.agregar_vertice(esquina)
		self.coord_metros[esquina] = np.array([x,y])
		self.coord_angulares[esquina] = np.array([lat,lon])

	def agregar_calle(self, idc, esquina1, esquina2):
		"""
		Agrega una calle que conecta las esquinas <esquina1> y <esquina2>
		"""
		dist = self.calcular_distancia(esquina1, esquina2)
		self.mapa.agregar_arista(esquina1, esquina2, dist, idc)

	def camino_optimo(self, esquina_inicio, esquina_fin):
		camino, distancia = self.mapa.camino_minimo(esquina_inicio, esquina_fin)
		return camino, distancia
