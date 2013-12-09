import operator

class Sistema:
    def __init__(self, pn, capacidad, mapa, juguetes, fabricas):
		self.polo_norte = pn
		self.capacidad_carrito = capacidad
		self.mapa = mapa
		self.juguetes = juguetes
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
				lista.append(idf+','+hora_ent+','+hora_sal)
				fin_ant = lista_fabricas[i].hora_salida
				cant += 1
		
		print('Cantidad: {}').format(cant)
		for i in range(len(lista)):
			print(lista[i])

    def valuar_carrito(self): return

    def valuar_juguetes_total(self): return

    def camino_optimo(self, idf): return

    def listar_juguetes(self, idf): return

    def graficar_rutas(self, idf): return

