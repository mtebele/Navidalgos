#!/usr/bin/env python

import sys
import csv
import juguete
import ciudad
import fabrica
import sistema

def cargar_fabricas():
	with open('fabricas.csv', 'rb') as archivo_f:
		archivo_csv = csv.reader(archivo_f)
		lista_fabricas = []		
		for idf, ide, hora_entrada, hora_salida in archivo_csv:
			fab = fabrica.Fabrica(idf, ide, hora_entrada, hora_salida)
			lista_fabricas.append(fab)
	archivo_f.close()
	return lista_fabricas

def cargar_juguetes():
	with open('juguetes.csv', 'rb') as archivo_j:
		archivo_csv = csv.reader(archivo_j)
		lista_juguetes = []		
		for idf, idj, valor, peso in archivo_csv:
			jug = juguete.Juguete(idf, idj, int(valor), int(peso))
			lista_juguetes.append(jug)
	archivo_j.close()
	return lista_juguetes

def cargar_mapa():
	with open('mapa.csv', 'rU') as archivo_c:
		archivo_csv = csv.reader(archivo_c)
		mapa = Ciudad()
		cant_esquinas = int(archivo_csv.next()[0])
		for i in range(cant_esquinas):
			lista = archivo_csv.next()
			ide = lista[0]
			x = float(lista[1])
			y = float(lista[2])
			latitud = float(lista[3])
			longitud = float(lista[4])
			mapa.agregar_esquina(ide, x, y, latitud, longitud)
		cant_calles = int(archivo_csv.next()[0])
		for j in range(cant_calles):
			lista = archivo_csv.next()
			idc = lista[0]
			esq_inicio = lista[1]
			esq_fin = lista[2]
			city.agregar_calle(idc, esq_inicio, esq_fin)
	archivo_c.close()
	return mapa

def main():	
	polo = int(sys.argv[1]);
	capacidad = int(sys.argv[2]);
	lista_fabricas = []
	mapa = ""
	lista_juguetes = []
	for i in range(len(sys.argv)-3):
		if sys.argv[i+3] == '/home/tebele/Desktop/TP3/pruebas/fabricas.csv': #corregir esta mierda
			lista_fabricas = cargar_fabricas()
		elif sys.argv[i+3] == 'juguetes.csv':
			lista_juguetes = cargar_juguetes()
		elif sys.argv[i+3] == 'mapa.csv':
			mapa = cargar_mapa()
			
	sis = sistema.Sistema(polo, capacidad, ciudad, lista_juguetes, lista_fabricas)
			
	#print('CARGA FINALIZADA')
	
	while True:
		linea = sys.stdin.readline()
		if not linea:
		   break
		pos_espacio = linea.find(' ')
		if pos_espacio == -1:
			comando = linea.rstrip('\n')
			parametros = []
		else:
			comando = linea[:pos_espacio]
			resto_linea = linea[pos_espacio+1:]
			parametros = resto_linea.split(",")
		
		instruccion = (comando, parametros)
		
		#COMIENZO INSTRUCCIONES#
		if instruccion[0] == 'listar_fabricas':
			sis.listar_fabricas()		
		
main()
