import operator
from grafo import Grafo
from ciudad import Ciudad
from fabrica import Fabrica

class Sistema:
    def __init__(self, pn, capacidad, ciudad, fabricas):
		self.polo_norte = pn
		self.capacidad_carrito = capacidad
		self.ciudad = ciudad
		self.fabricas = fabricas
		self.fabricas_visitar = None
	
    def listar_fabricas(self):
		"""
		Devuelve las fabricas optimas en cuanto a cantidad de fabricas visitadas. 
		"""																	
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
		"""
		Devuelve el valor de sonrisas correspondiente a la combinacion de 
		juguetes optima a retirar de la fabrica <idf>
		"""
		if idf < 0 or idf >= len(self.fabricas):
			print('Error: la fabrica con id {} no existe').format(idf)
			return
		fabrica = self.fabricas[idf]
		row = []
		res = []
		cantidad_maxima = len(fabrica.juguetes)
		fabrica.juguetes.sort(key=operator.attrgetter('idj'))
		
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
		"""
		Devuelve los valores de sonrisas optimos para todas las fabricas 
		a visitar
		"""
		if self.fabricas_visitar is None:
			self.listar_fabricas()
		total_sonrisas = 0
		for f in self.fabricas_visitar:
			total_sonrisas += self.valuar_juguetes(int(f.idf))
		return total_sonrisas

    def camino_optimo(self, idf):
		"""
		Devuelve la distancia optima desde la fabrica <idf> hasta el polo norte
		y las coordenadas angulares del recorrido efectuado.
		"""
		fin = self.polo_norte
		fabrica = self.fabricas[int(idf)]
		inicio = fabrica.obtener_esquina()
		camino, distancia = self.ciudad.camino_optimo(inicio, fin)
		coordenadas = []
		for c in camino:
			coordenadas.append(self.ciudad.coordenadas_angulares(c))
		return coordenadas, distancia

    def listar_juguetes(self, idf):
		"""
		Devuelve la lista de juguetes y el valor de sonrisas correspondiente 
		a la combinacion optima a retirar de la fabrica <idf>
		"""
		valor,res = self.valuar_juguetes(idf, True)
		fabrica = self.fabricas[idf]
		juguetes = fabrica.juguetes
		lista = []		
		w = self.capacidad_carrito
		j = len(juguetes)-1
		
		while j >= 0 and w >= 0:
			agregado = res[j][w] != res[j-1][w]
			if agregado:
				jug = juguetes[j]
				w -= jug.peso
				if w < 0:
					break
				lista.append(jug)	
			j-=1
			
		lista.reverse()
		return valor,lista

    def graficar_rutas(self, idf):
		coordenadas, distancia = self.camino_optimo(idf)
		f = open(idf+'.kml', 'w')
		f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
		f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\"\n")
		f.write("xmlns:gx=\"http://www.google.com/kml/ext/2.2\"\n")
		f.write("xmlns:kml=\"http://www.opengis.net/kml/2.2\"\n")
		f.write("xmlns:atom=\"http://www.w3.org/2005/Atom\">\n")
		f.write("<Document>\n")
		linea = ("	<name> {} </name>\n").format(idf)
		f.write(linea)
		f.write("		<Placemark>\n")
		f.write("			<name> Viaje a fabrica </name>\n")
		linea = ("			<description> Recorrido de la fabrica {} </description>\n").format(idf)
		f.write(linea)
		f.write("			<LineString>\n")
		f.write("				<coordinates>\n")
		for c in coordenadas:
			linea = ("					{},{}\n").format(c[0], c[1])
			f.write(linea)
		f.write("			</coordinates>\n")
		f.write("		</LineString>\n")
		f.write("	</Placemark>\n")		
		
		f.write("	<Placemark>\n")
		f.write("		<name>Polo Norte</name>\n")
		f.write("		<description> Papa Noel </description>\n")
		f.write("		<Point>\n")
		polo = self.ciudad.coordenadas_angulares(str(self.polo_norte))
		linea = ("			<coordinates>{},{}</coordinates>\n").format(polo[0],polo[1])
		f.write(linea)
		f.write("		</Point>\n")
		f.write("	</Placemark>\n")

		f.write("	<Placemark>\n")
		linea = ("		<name>{}</name>\n").format(idf)
		f.write(linea)
		f.write("		<description> Juguetes! </description>\n")
		f.write("		<Point>\n")
		fabrica = self.fabricas[int(idf)]
		esquina = fabrica.obtener_esquina()		
		polo = self.ciudad.coordenadas_angulares(str(esquina))
		linea = ("			<coordinates>{},{}</coordinates>\n").format(polo[0],polo[1])
		f.write(linea)
		f.write("		</Point>\n")
		f.write("	</Placemark>\n")
		f.write("</Document>\n")
		f.write("</kml>\n")	
		f.close()
