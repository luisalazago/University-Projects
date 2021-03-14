"""
********************************************************************************************************
Autor: Luis Alberto Salazar Gómez.
Código: 8950100.
Frase de Compromiso: Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali
					 me comprometo a seguir los más altos estándares de integridad académica.
********************************************************************************************************
"""

from sys import stdin
from heapq import heappop, heappush
import collections

INFINITO = float('inf')

peso = {} # El peso es global ya que cambia tanto en el main como en el reocorrido del laberinto.

def recorridoLaberinto(maze, traductor, s):
	"""
	Entrada: Un mapa que cumple función del grafo del laberinto, un vector que tiene el id de cada
			 símbolo original del laberinto, un mapa que contiene el peso de cada nodo utilizado en
			 el grafo y finalmente un nodo donde inicia el seguiemiento del algoritmo.
	Salida: La impresión del total del camino recorrido para encontrar a acada alienigena.
	"""
	global peso
	peso[s], total = 0, 0
	espacios = [(0, s)] # Se usa esta estructura de montículo para simular una cola de prioridad.
	espacios2 = collections.deque([])

	visitados = {}
	for n in peso:
		visitados[n] = -1

	"""
	Esto es un Dijkstra que ejecuta primero un BFS para encontrar los mejores caminos hacia
	cada alienigena, es decir, el montículo solo almacena el nodo de inicio y los demás
	nodos alienigenas, usa un BFS aunque si encuentra un Alien usa la misma condición que el
	algoritmo de Dijkstra para asegurarse de que siempre encuentre el camino más corto. En pocas
	palabras se aplica del algoritmo de Dijkstra desde cada Alien que esté en el laberinto.
	"""

	while(len(espacios) != 0):
		p, u = heappop(espacios)
		if(p == peso[u]):
			total += p # Aquí se añaden los mejores pasos encontrados.
			peso[u] = -1 # Como pueden haber más de un camino para un mismo Alien con esto se asegura que no cambie el mejor camino encontrado ni que se añadan otra vez los mismos nodos a la cola de prioridad.
			for n in visitados:
				visitados[n] = -1
			espacios2.append(u)
			visitados[u] = 0
			while(len(espacios2) != 0):
				v = espacios2.popleft()

				i = 0
				while(i < len(maze[v])):
					nodo = maze[v][i]
					if(visitados[nodo] == -1):
						visitados[nodo] = visitados[v] + 1 # Se le va sumando 1 por cada nivel que suba.
						espacios2.append(nodo)
						if(traductor[nodo] == "A" and visitados[nodo] < peso[nodo]):
							peso[nodo] = visitados[nodo]
							heappush(espacios, (peso[nodo], nodo))
					i += 1
	print(total)


def main():
	global peso
	lectura = stdin.readlines()
	i = 0
	casos = int(lectura[i])
	i += 1
	j = 0
	while(j < casos):
		lectura[i] = lectura[i].strip()
		columnas, filas = lectura[i].split()
		columnas = int(columnas)
		filas = int(filas)
		maze_1 = [[None for m in range(columnas)] for n in range(filas)]
		traductor = [None for n in range(filas * columnas)] # Con esta estructura se sabe el id de cada símbolo del laberinto (llave primaria).
		pos_inicalx, pos_inicaly = -1, -1 # Con esto el algoritmo se asegura que existen nodos por los cuales moverse en el laberinto.
		i += 1

		k, pos = 0, 0
		while(k < filas):
			l = 0
			while(l < columnas):
				if(lectura[i][l] != "#"):
					if(lectura[i][l] == "S"):
						pos_inicalx = k # Posición inicial en la fila.
						pos_inicaly = l # Posición inicial en la columna.
					traductor[pos] = lectura[i][l] # Se llena el vector que trae el valor original del número (símbolo).
					maze_1[k][l] = str(pos)
				else:
					maze_1[k][l] = lectura[i][l]
				pos += 1
				l += 1
			k += 1
			i += 1

		maze = {} # Se usó un diccionario para manejar más fácil los nodos que contiene y no tener espacion demás, además contiene un lista en los cuales se encuentran los nodos adyacentes de cada nodo.

		if(pos_inicalx != -1 and pos_inicaly != -1):

			"""
			Aquí se transforma la matriz de strings en un grafo con valores númericos, ya que es más fácil trabajar
			con números que con cualquier otra cosa, entonces se mira la posición actual y de ahí se analiza tanto
			a la izquierda como a la derecha, tanto arriba como abajo, si puede formar el grafo a partir de ese 
			análisis, eso se logra viendo si la siguiente posición es diferente de "$" y que la posición actual también
			lo sea, si la posición que se mira es diferente de "$" y de "#" entonces se pasa a añadirla al grafo además
			de añadirla a la cola para procesarla, así sucesivamente con todos los nodos. Cómo en este caso se usa un
			diccionario vacío, se tiene que analizar si la key ya está dentro de él o si no, si no existe entonces se
			crea una lista para almacenar los nodos, si existe dentro del diccionario entonces se procede a añadirlo
			a la lista ya existente dentro de él.
			"""

			s = -1
			puntos = collections.deque([])
			puntos.append([pos_inicalx, pos_inicaly])
			while(len(puntos) != 0):
				temp1 = puntos[0][0]
				temp2 = puntos[0][1]
				puntos.popleft()
				if(maze_1[temp1][temp2] != "$"): numero2 = int(maze_1[temp1][temp2])
				else: numero2 = "$"
				if(temp1 == pos_inicalx and temp2 == pos_inicaly and numero2 != "$"): s = numero2 # Posición inicial.

				# Mira derecha
				if(maze_1[temp1][temp2 + 1] != "#" and maze_1[temp1][temp2 + 1] != "$" and numero2 != "$"):
					k = int(maze_1[temp1][temp2 + 1])
					if(numero2 in maze): maze[numero2].append(k)
					else: maze[numero2] = [k] 
					
					if(k in maze): maze[k].append(numero2)
					else: maze[k] = [numero2] 
					puntos.append([temp1, temp2 + 1])

				# Mira Izquierda
				if(maze_1[temp1][temp2 - 1] != "#" and maze_1[temp1][temp2 - 1] != "$" and numero2 != "$"):
					k = int(maze_1[temp1][temp2 - 1])
					if(numero2 in maze): maze[numero2].append(k)
					else: maze[numero2] = [k] 
					
					if(k in maze): maze[k].append(numero2)
					else: maze[k] = [numero2] 
					puntos.append([temp1, temp2 - 1])

				# Mira Arriba
				if(maze_1[temp1 + 1][temp2] != "#" and maze_1[temp1 + 1][temp2] != "$" and numero2 != "$"):
					k = int(maze_1[temp1 + 1][temp2])
					if(numero2 in maze): maze[numero2].append(k)
					else: maze[numero2] = [k] 
					
					if(k in maze): maze[k].append(numero2)
					else: maze[k] = [numero2] 
					puntos.append([temp1 + 1, temp2])

				# Mira abajo
				if(maze_1[temp1 - 1][temp2] != "#" and maze_1[temp1 - 1][temp2] != "$" and numero2 != "$"):
					k = int(maze_1[temp1 - 1][temp2])
					if(numero2 in maze): maze[numero2].append(k)
					else: maze[numero2] = [k] 
					
					if(k in maze): maze[k].append(numero2)
					else: maze[k] = [numero2] 
					puntos.append([temp1 - 1, temp2])

				maze_1[temp1][temp2] = "$" # Con esto se asegura el algoritmo que el nodo actual ya fue añadido al grafo, con sus nodos adyacentes.

			peso = {}
			for n in maze:
				peso[n] = INFINITO

			recorridoLaberinto(maze, traductor, s)

		else:
			print(0)

		j += 1
main()

"""
La complejidad de este algoritmo tiene varias partes, primero, en la construcción del grafo se hace en 
O(n), luego en la partes del cálculo de la solución se hace un BFS por cada Alien es decir es O(n) * O(nlog(n)),
donde O(nlog(n)) es el algoritmo de Dijsktra y O(n), esto al final en el peor de los casos es O(n^2), lo cual
no lo hace un algoritmo tan eficiente como se esperaría, aún así tiene un ventaja y es que el algoritmo es fácil
de manejar puesto a que se tiene un grafo construido y se conoce bien cada posición y lo que trae del laberinto
original.
"""