import csv
from juguete import Juguete
from ciudad import Ciudad
from ciudad import Esquina

def main():
	with open('juguetes.csv', 'rb') as archivo_j:
		archivo_csv = csv.reader(archivo_j)
		lista_juguetes = []		
		for idf, idj, valor, peso in archivo_csv:
			jug = Juguete(idf, idj, int(valor), int(peso))
			lista_juguetes.append(jug)
	archivo_j.close()

	with open('fabricas.csv', 'rb') as archivo_f:
		archivo_csv = csv.reader(archivo_f)
		ciudad = Ciudad()
		for ide, x, y, latitud, longitud in archivo_csv:
			esquina = Esquina(ide, int(x), int(y), float(latitud), float(longitud))
			ciudad.agregar_esquina(esquina)
			
main()
