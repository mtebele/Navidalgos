import operator
from grafo import Grafo
from ciudad import Ciudad

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
		
    def valuar_juguetes(self, idf, listar_juguetes = False):
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
			
		for c in range(cantidad_maxima):
			for p in range(self.capacidad_carrito+1):
				p_nuevo = fabrica.juguetes[c].peso
				v_nuevo = fabrica.juguetes[c].valor
				if p >= p_nuevo:
					res[c][p] = max(res[c-1][p], res[c-1][p-p_nuevo] + v_nuevo)
				else:
					res[c][p] = res[c-1][p]
		
		valor = res[cantidad_maxima-1][self.capacidad_carrito]
		
		if listar_juguetes == True:
			return valor,res
		return valor
    
    def valuar_juguetes_total(self):
		if self.fabricas_visitar is None:
			self.listar_fabricas()
		total_sonrisas = 0
		for f in self.fabricas_visitar:
			total_sonrisas += self.valuar_juguetes(f.idf)
		return total_sonrisas

    def camino_optimo(self, idf):
		fin = self.polo_norte
		camino, distancia = self.ciudad.camino_optimo(idf, fin)
		return camino, distancia #aca obtenemos los nombres de las ciudades nada mas, habria que darle formato.
		
    def listar_juguetes(self, idf):
		valor,res = self.valuar_juguetes(idf, True)
		fabrica = self.fabricas[idf]
		juguetes = fabrica.juguetes
		
		lista = []
		w = self.capacidad_carrito
		for j in range(len(juguetes)-1, 0, -1):
			agregado = res[j][w] != res[j-1][w]
			if agregado:
				jug = juguetes[j]
				lista.append(jug)
				w -= jug.peso

		lista.reverse()
		return valor,lista

    def graficar_rutas(self, idf): return
    
