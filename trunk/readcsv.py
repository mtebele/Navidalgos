#!/usr/bin/env python

import csv
from juguete import Juguete
from ciudad import Ciudad
from esquina import Esquina

def main():
	with open('juguetes.csv', 'rb') as archivo_j:
		archivo_csv = csv.reader(archivo_j)
		lista_juguetes = []		
		for idf, idj, valor, peso in archivo_csv:
			jug = Juguete(idf, idj, int(valor), int(peso))
			lista_juguetes.append(jug)
	archivo_j.close()

	with open('mapa.csv', 'rb') as archivo_c:
		archivo_csv = csv.reader(archivo_c)
		ciudad = Ciudad()
		cant_esquinas = int(archivo_csv.next())
		for i in range(cant_esquinas):
			lista = archivo_csv.next()
			ide = lista[0]
			x = float(lista[1])
			y = float(lista[2])
			latitud = int(lista[3])
			longitud = int(lista[4])
			ciudad.agregar_esquina(ide, x, y, latitud, longitud)
		cant_calles = int(archivo_csv.next())
		for j in range(cant_calles):
			lista = archivo_csv.next()
			idc = lista[0]
			esq_inicio = lista[1]
			esq_fin = lista[2]
			ciudad.agregar_calle(esq_inicio, esq_fin, idc)
	archivo_c.close()	
			
main()
