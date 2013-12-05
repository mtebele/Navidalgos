import csv
from juguete import Juguete

def main():
	with open('juguetes.csv', 'rb') as archivo:
		archivo_csv = csv.reader(archivo)
		lista_juguetes = []		
		for idf, idj, valor, peso in archivo_csv:
			jug = Juguete(idf, idj, valor, peso)
			lista_juguetes.append(jug)
	archivo.close()
main()
