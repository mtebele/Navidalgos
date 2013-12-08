#!/usr/bin/env python

import sys
import csv
import juguete
import ciudad
import fabrica

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
	return city

def validar_instruccion(instruccion):
	"""Valido si la instruccion tiene formato correcto"""
	validos = { "listar_fabricas" : 0,
                "valuar_juguetes" : 1,
                "valuar_juguetes_total" : 0,
                "camino_optimo" : 1,
                "listar_juguetes" : 1,
                "entrenar_duendes" : 1,
                "graficar_rutas" : 1,
	}
	if instruccion[0] in validos.keys():
		return validos[instruccion[0]] == len(instruccion[1])
	else: 	
		return False

def main():
	
	polo = int(sys.argv[1]);
	capacidad = int(sys.argv[2]);
	for i in range(len(sys.argv)-3):
		if sys.argv[i+3] == 'fabricas.csv':
			cargar_fabricas()
		elif sys.argv[i+3] == 'juguetes.csv':
			cargar_juguetes()
		elif sys.argv[i+3] == 'mapa.csv':
			cargar_mapa()
	
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
		instruccion = (comando,parametros)
		if validar_instruccion(instruccion):
			print "Comando valido"
		else: print "Comando Invalido" 
main()
