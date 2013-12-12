class Fabrica:
    def __init__(self, idf, ide, hor1, hor2):
		self.idf = int(idf)
		self.ide = int(ide)
		self.hora_entrada = int(hor1)
		self.hora_salida = int(hor2)
		self.juguetes = []

    def duracion(self):
		"""
		Determina la duracion de estadia en la fabrica
		"""
		return hora_entrada - hora_salida

    def agregar_juguete(self, juguete):
		"""
		Agrega un juguete a la fabrica
		"""
		self.juguetes.append(juguete)
	
    def obtener_esquina(self):
		"""
		Devuelve la esquina en la que esta ubicada la fabrica
		"""
		return str(self.ide)
