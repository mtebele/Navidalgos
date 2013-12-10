class Fabrica:
    def __init__(self, idf, ide, hor1, hor2):
		self.idf = int(idf)
		self.ide = int(ide)
		self.hora_entrada = int(hor1)
		self.hora_salida = int(hor2)
		self.juguetes = []

    def duracion(self):
		return hora_entrada - hora_salida

    def agregar_juguete(self, juguete):
		self.juguetes.append(juguete)
