import operator

class Sistema:
    def __init__(self, pn, capacidad, mapa, fabricas):
		self.polo_norte = pn
		self.capacidad_carrito = capacidad
		self.mapa = mapa
		self.fabricas = fabricas
	
    def listar_fabricas(self):
		lista_fabricas = sorted(self.fabricas, key=operator.attrgetter('hora_salida', 'hora_entrada'))
		lista = []
		cant = 0
		fin_ant = -1
		for i in range(len(lista_fabricas)):
			if lista_fabricas[i].hora_entrada >= fin_ant:
				idf = lista_fabricas[i].idf
				hora_ent = '{:02d}:{:02d}'.format(*divmod(lista_fabricas[i].hora_entrada, 60))
				hora_sal = '{:02d}:{:02d}'.format(*divmod(lista_fabricas[i].hora_salida, 60))			
				lista.append('{},{},{}'.format(idf, hora_ent, hora_sal))
				fin_ant = lista_fabricas[i].hora_salida
				cant += 1
		
		print('Cantidad: {}').format(cant)
		for i in range(len(lista)):
			print(lista[i])

    def valuar_juguetes(self, idf):
		if idf >= len(self.fabricas):
			print('Error: la fabrica con id ' + idf + ' no existe')
			return
		fabrica = self.fabricas[idf]
		res = []
		cantidad_maxima = len(fabrica.juguetes)
		
		for cant in range(cantidad_maxima+1):
			res.append({})
		for peso in range(self.capacidad_carrito+1):
			res[0][peso] = 0
		for c in range(1, cantidad_maxima):
			for p in range(self.capacidad_carrito+1):
				p_nuevo = fabrica.juguetes[c].peso
				v_nuevo = fabrica.juguetes[c].valor
				if p >= p_nuevo:
					res[c][p] = max(res[c-1][p], res[c-1][p-p_nuevo] + v_nuevo)
				else:
					res[c][p] = res[c-1][p]
		
		valor = res[cantidad_maxima-1][self.capacidad_carrito]
		return valor
    
    def valuar_juguetes_total(self):
		total_sonrisas = 0
		for f in self.fabricas:
			total_sonrisas += self.valuar_juguetes(f.idf)
		return total_sonrisas

    def camino_optimo(self, idf): return

    def listar_juguetes(self, idf): return

    def graficar_rutas(self, idf): return

