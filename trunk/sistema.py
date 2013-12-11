import operator
from grafo import Grafo

class Sistema:
    def __init__(self, pn, capacidad, ciudad, fabricas):
		self.polo_norte = pn
		self.capacidad_carrito = capacidad
		self.ciudad = ciudad
		self.fabricas = fabricas
		self.fabricas_visitar = None
	
    def listar_fabricas(self):																											
		lista_fabricas = sorted(self.fabricas, key=operator.attrgetter('hora_salida', 'hora_entrada'))
		lista = []
		lista_visitar = []
		cant = 0
		fin_ant = -1
		for i in range(len(lista_fabricas)):
			if lista_fabricas[i].hora_entrada >= fin_ant:
				idf = lista_fabricas[i].idf
				hora_ent = '{:02d}:{:02d}'.format(*divmod(lista_fabricas[i].hora_entrada, 60))
				hora_sal = '{:02d}:{:02d}'.format(*divmod(lista_fabricas[i].hora_salida, 60))			
				lista.append('{},{},{}'.format(idf, hora_ent, hora_sal))
				lista_visitar.append(lista_fabricas[i])
				fin_ant = lista_fabricas[i].hora_salida
				cant += 1
		
		self.fabricas_visitar = lista_visitar
		return lista
		
    def valuar_juguetes(self, idf):
		if idf >= len(self.fabricas):
			print('Error: la fabrica con id ' + idf + ' no existe')
			return
		fabrica = self.fabricas[idf]
		row = []
		res = []
		cantidad_maxima = len(fabrica.juguetes)
		
		for i in range(self.capacidad_carrito+1):
			row.append(0)
		for i in range(cantidad_maxima):
			res.append(row[:])
			
		for c in range(0,cantidad_maxima):
			for p in range(0,self.capacidad_carrito+1):
				p_nuevo = fabrica.juguetes[c].peso
				v_nuevo = fabrica.juguetes[c].valor
				if p >= p_nuevo:
					res[c][p] = max(res[c-1][p], res[c-1][p-p_nuevo] + v_nuevo)
				else:
					res[c][p] = res[c-1][p]
		
		valor = res[cantidad_maxima-1][self.capacidad_carrito]
		return valor
    
    def valuar_juguetes_total(self):
		if self.fabricas_visitar is None:
			self.listar_fabricas()
		total_sonrisas = 0
		for f in self.fabricas_visitar:
			total_sonrisas += self.valuar_juguetes(f.idf)
		return total_sonrisas

    def camino_optimo(self, idf):
		mapa = self.ciudad.obtener_mapa()
		fin = self.polo_norte
		distancias, hijos = Grafo.dijkstra(mapa, idf, fin)
		print hijos
		camino = []
		while idf != fin:
			camino.append(fin)
			if idf == fin: break
			fin = hijos[fin]
		camino.reverse()
		return camino #aca obtenemos los nombres de las ciudades nada mas, habria que darle formato.
				
    def listar_juguetes(self, idf): return

    def graficar_rutas(self, idf): return

