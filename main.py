#!/usr/bin/env python

import sys
import csv
from juguete import Juguete
from ciudad import Ciudad
from fabrica import Fabrica
from sistema import Sistema

def cargar_fabricas(nomarch):
	"""
	Carga las fabricas con la informacion del archivo <nomarch>
	"""
	with open(nomarch, 'rb') as archivo_f:
		archivo_csv = csv.reader(archivo_f)
		lista_fabricas = []		
		for idf, ide, hora_entrada, hora_salida in archivo_csv:
			fab = Fabrica(idf, ide, hora_entrada, hora_salida)
			lista_fabricas.append(fab)
	archivo_f.close()
	return lista_fabricas

def cargar_juguetes(nomarch, lista_fabricas):
	"""
	Carga los juguetes con la informacion del archivo <nomarch> en las fabricas
	pertenecientes a <lista_fabricas>
	"""
	with open(nomarch, 'rb') as archivo_j:
		archivo_csv = csv.reader(archivo_j)	
		for idf, idj, valor, peso in archivo_csv:
			fab = lista_fabricas[int(idf)]
			jug = Juguete(idj, int(valor), int(peso))
			fab.juguetes.append(jug)
	archivo_j.close()

def cargar_ciudad(nomarch):
	"""
	Carga la ciudad con la informacion del archivo <nomarch>
	"""
	with open(nomarch, 'rU') as archivo_c:
		archivo_csv = csv.reader(archivo_c)
		ciudad = Ciudad()
		cant_esquinas = int(archivo_csv.next()[0])
		for i in range(cant_esquinas):
			lista = archivo_csv.next()
			ide = lista[0]
			x = float(lista[1])
			y = float(lista[2])
			latitud = float(lista[3])
			longitud = float(lista[4])
			ciudad.agregar_esquina(ide, x, y, latitud, longitud)
		cant_calles = int(archivo_csv.next()[0])
		for j in range(cant_calles):
			lista = archivo_csv.next()
			idc = lista[0]
			esq_inicio = lista[1]
			esq_fin = lista[2]
			ciudad.agregar_calle(idc, esq_inicio, esq_fin)
	archivo_c.close()
	return ciudad

def main():
	"""
	Bloque principal. Se carga en el sistema la capacidad del carrito,
	la ubicacion del polo norte, las fabricas con sus juguetes y la ciudad.
	Una vez realizado esto, se procede a leer los comandos que el usuario
	ingrese, ejecutando la operacion correspondiente en caso de ser necesario.
	"""
	capacidad = int(sys.argv[1]);
	polo = int(sys.argv[2]);
	lista_fabricas = cargar_fabricas(sys.argv[3])
	cargar_juguetes(sys.argv[4], lista_fabricas)
	ciudad = cargar_ciudad(sys.argv[5])
			
	sis = Sistema(polo, capacidad, ciudad, lista_fabricas)
	
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
		
		# Comienzo de instrucciones
		if instruccion[0] == 'listar_fabricas':
			lista = sis.listar_fabricas()	
			print('Cantidad: {}').format(len(lista))
			for i in range(len(lista)):
				print(lista[i])
		elif instruccion[0] == 'valuar_juguetes':
			idf = int(instruccion[1][0].rstrip('\n'))
			valor = sis.valuar_juguetes(idf)
			if (valor is not None):
				print('Total: {} Sonrisas').format(valor)
		elif instruccion[0] == 'valuar_juguetes_total':
			valor = sis.valuar_juguetes_total()
			if (valor is not None):
				print('Total: {} Sonrisas').format(valor)
		elif instruccion[0] == 'camino_optimo':
			idf = instruccion[1][0].rstrip('\n')
			coordenadas, distancia = sis.camino_optimo(idf)
			print('Distancia: {} Metros').format(int(distancia))			
			for i in range(len(coordenadas)):
				print('{},{}').format(coordenadas[i][0],coordenadas[i][1])
		elif instruccion[0] == 'graficar_rutas':
			idf = instruccion[1][0].rstrip('\n')
			sis.graficar_rutas(idf)
			print 'OK'
		elif instruccion[0] == 'listar_juguetes':
			idf = int(instruccion[1][0].rstrip('\n'))
			valor, lista = sis.listar_juguetes(idf)
			if (valor is not None):
				print('Total: {} Sonrisas').format(valor)
				for j in range(len(lista)):
					print(lista[j].idj)
		else:
			print 'Comando Invalido. Intente nuevamente.'	
		
main()
