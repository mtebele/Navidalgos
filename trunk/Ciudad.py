import grafo
import math

class Esquina:
    def __init__(self, ide, x1, y1, lon, lat):
		self.id = ide
		self.x = x1
		self.y = y1
		self.longitud = lon
		self.latitud = lat
		
	def calcular_distancia(self, esquina2):
		dist_x = esquina2.x - self.x
		dist_y = esquina2.y - self.y	
		return math.hypot(dist_x, dist_y)

	def coordenadas(self)
		return (self.longitud, self.latitud)
			
class Ciudad:
	def __init__(self):
		self.mapa = Grafo()
		self.cant_esquinas = 0
		self.cant_calles = 0

	def agregar_esquina(self, esquina):
		self.mapa.agregar_vertice(esquina)
		self.cant_esquinas += 1

	def agregar_calle(self, esquina1, esquina2):
		dist  =  esquina1.calcular_distancia(esquina2)
		self.mapa.agregar_arista(esquina1, esquina2, dist)
		self.cant_calles += 1
