#!/usr/bin/env python

import csv
import juguete
import ciudad
import fabrica

def main():
	print(">> ARRANCA")
	with open('fabricas.csv', 'rb') as archivo_f:
		archivo_csv = csv.reader(archivo_f)
		lista_fabricas = []		
		for idf, ide, hora_entrada, hora_salida in archivo_csv:
			fab = fabrica.Fabrica(idf, ide, hora_entrada, hora_salida)
			lista_fabricas.append(fab)
	archivo_f.close()
	
	with open('juguetes.csv', 'rb') as archivo_j:
		archivo_csv = csv.reader(archivo_j)
		lista_juguetes = []		
		for idf, idj, valor, peso in archivo_csv:
			jug = juguete.Juguete(idf, idj, int(valor), int(peso))
			lista_juguetes.append(jug)
	archivo_j.close()

	with open('mapa.csv', 'rU') as archivo_c:
		archivo_csv = csv.reader(archivo_c)
		city = ciudad.Ciudad()
		cant_esquinas = int(archivo_csv.next()[0])
		for i in range(cant_esquinas):
			lista = archivo_csv.next()
			ide = lista[0]
			x = float(lista[1])
			y = float(lista[2])
			latitud = float(lista[3])
			longitud = float(lista[4])
			city.agregar_esquina(ide, x, y, latitud, longitud)
		cant_calles = int(archivo_csv.next()[0])
		for j in range(cant_calles):
			lista = archivo_csv.next()
			idc = lista[0]
			esq_inicio = lista[1]
			esq_fin = lista[2]
			city.agregar_calle(idc, esq_inicio, esq_fin)
	archivo_c.close()
	print(">> TERMINA")
			
main()
