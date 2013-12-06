import sys

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
