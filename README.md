# Navidalgos

## Estructuras de datos implementadas
Hicimos uso de las siguientes estructuras previamente implementadas:
### Grafo
El grafo se utiliza para representar el mapa, con sus esquinas y calles
correspondientes.
### Diccionario
Los diccionarios son empleados en la representación matricial del Grafo
y para referenciar información de las esquinas del mapa (coordenadas).
### Lista
Utilizamos listas para almacenar los resultados que arroja el sistema en
caso de los servicios que solicitan listados.
### Ciudad
Estructura encargada de modelar las conexiones entre las esquinas.
### Fabrica
En la misma se almacenan los juguetes. Poseen un identificador y una
ubicación en la ciudad.
### Juguete
Los juguetes a repartir poseen un valor de sonrisas, un peso y un identi-
ficador.
## Flujo del programa
El programa recibe archivos csv, los cuales son procesados en el programa
principal.
### Interacción con el usuario
El principal obtendrá la información de los archivos y la organizará en
estructuras que permitirán el fácil acceso a la información. Una vez procesados
son cerrados y el programa iniciará el proceso de lectura de la entrada
estándar, esperando que se ingresen los comandos en la misma. El usuario
enviará instrucciones al programa respetando el estándar especificado en el
enunciado del TP.
### Interpretación de las instrucciones recibidas por
el usuario
Cada línea de texto (secuencia de caracteres finalizada con ENTER)
será la instrucción a interpretar. Internamente, el programa almacena la línea
en una cadena, que posteriormente es dividida en secciones. La primera secci
ón es considerada el comando a realizar, mientras que el resto de la cadena
representará el/los parámetros con los que operará el comando. De acuerdo a
lo explicado en la subsección anterior, el programa validará el comando y posteriormente
hará lo mismo con la relación comando - cantidad de parámetros.
### Ejecución de las instrucciones
Una vez que los comandos y parámetros fueron validados correctamente,
el programa procede a ejecutar la función correspondiente al comando ingresado.
Una vez realizada la ejecución del servicio, el programa emite un
mensaje desde la salida estándar, dependiendo éste del servicio solicitado.
### Fin de la ejecución
El programa finaliza al recibir en la entrada una señal de fin de archivo.
## Resolución de los problemas planteados
### Listar fábricas
Solución: Se crea una lista de fábricas ordenada ascendentemente por
hora de salida y hora de entrada, en ese orden de prioridad. Utilizando
un algoritmo Greedy, se selecciona la fábrica con menor horario de
salida, siempre y cuando el mismo no se superponga con el horario de
las seleccionadas previamente. Los datos solicitados de las fábricas a
visitar son devueltos en una lista.
Orden: Considerando el ordenamiento inicial de las fábricas de manera
lineal (desconocemos cómo lo hace python, pero podría hacerse con
alguna de las técnicas de ordenamiento lineal que hemos visto en clase),
podemos decir que el orden del algoritmo es lineal, puesto que el mismo
solamente trata con operaciones constantes (asignación, comparación)
a cada una de las fábricas en la ciudad.
### Valuar juguetes
Solución: Se busca la fábrica con el identificador recibido por parámetro
(levantando un mensaje de error en caso de que no exista tal fábrica).
Luego, empleando programación dinámica guarda en una matriz los
mejores resultados según las capacidades menores o iguales a la capacidad
del carrito para la cual se pretende obtener el resultado óptimo, y
según la cantidad de juguetes posibles. El resultado consultado termina
siendo almacenado en la matriz, por lo que el algoritmo devuelve dicho
resultado accediendo a la misma.
Orden: La búsqueda de la fábrica es lineal sobre 'f', siendo 'f' la cantidad
de fábricas del sistema. Posteriormente se realizan 'c' veces las 'j'
operaciones correspondientes a los resultados óptimos de los subproblemas,
siendo 'c' la capacidad del carrito y 'j' la cantidad de juguetes
de la fábrica. El resto de las operaciones son constantes. Consideramos
que la búsqueda de la fábrica puede omitirse, teniendo en cuenta el orden
superior del problema de programación dinámica. Luego, el orden
es O(c*j)
### Valuar juguetes total
Solución: Aplicamos la funcion valuar juguetes para todas las fabricas
a visitar
Orden: O(n*(c*j)), siendo n la cantidad de fábricas a visitar y el resto
de los valores, los mencionados en el ítem previo.
### Camino óptimo
Solución: Para resolver este problema, utilizamos el algoritmo de Dijkstra,
partiendo desde el polo norte hasta la fábrica solicitada. El camino
es expresado en una lista.
Orden: Al aplicar Dijkstra, el orden de este algoritmo es
O((C+E)logE), siendo E la cantidad de esquinas del mapa y C la cantidad
de calles. El orden de armar el listado correspondiente al camino
mínimo es despreciable.
### Listar Juguetes
Solución: Se busca la fábrica con el identificador recibido por parámetro
(levantando un mensaje de error en caso de que no exista tal fábrica).
Luego, empleando programación dinámica se guarda en una matriz los
mejores resultados según las capacidades menores o iguales a la capacidad
del carrito para la cual se pretende obtener el resultado óptimo, y
según la cantidad de juguetes posibles. Luego, se recorre la matriz de
modo inverso en busca de los juguetes que fueron seleccionados en el
algoritmo previo, almacenándolos en una lista que se devolverá junto
al resultado almacenado en la matriz.
Orden: la búsqueda de la fábrica es lineal sobre 'f', siendo 'f' la cantidad
de fábricas del sistema. Luego se realizan 'c' veces las 'j' operaciones
correspondientes a los resultados óptimos de los subproblemas, siendo
'c' la capacidad del carrito y 'j' la cantidad de juguetes de la fábrica.
Luego, se recorre la matriz linealmente según la cantidad de juguetes
pertenecientes a la fábrica. El resto de las operaciones son constantes.
Los recorridos lineales antes mencionados son despreciables. Luego, el
orden es O(c*j).
### Graficar Rutas
Solución: Primero se emplea la función camino óptimo para obtener las
coordenadas correspondientes al camino desde la fabrica consultada
hasta el polo norte.
Orden: Como mencionamos en incisos previos, el orden de camino óptimo
es O((C+E)logE), siendo E la cantidad de esquinas y C la cantidad
de calles del mapa. Luego, se efectuan operaciones constantes (escritura
en archivo, asignación), salvo por la iteracion sobre las coordenadas
para crear la LineString, la cual es despreciable considerando que el
orden de camino óptimo es mayor. Luego, el orden del algoritmo es
O((C+E)logE).
