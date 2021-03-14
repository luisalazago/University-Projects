/*********************************************************************************************************
* Autor: Luis Alberto Salazar Gómez.
* Código: 8950100.
* Frase de Compromiso: Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali 
					   me comprometo a seguir los más altos estándares de integridad académica.	  
*********************************************************************************************************/


#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <queue>
#include <sstream>
#include <map>
#include <set>

#define endl '\n'
#define INFINITO 20000000

using namespace std;

void recorridoLaberinto(map<int, set<int>>& maze, vector<string>& traductor, map<int, int>& peso, int s) {
	/* Entrada: Un mapa que cumple función del grafo del laberinto, un vector que tiene el id de cada
				símbolo original del laberinto, un mapa que contiene el peso de cada nodo utilizado en
				el grafo y finalmente un nodo donde inicia el seguiemiento del algoritmo.
	   Salida: La impresión del total del camino recorrido para encontrar a acada alienigena. */
	int v, u, p, nodo, total;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> espacios; // Cola de prioridad que comprar y ordena con respecto a la menor pareja iniciando por el peso. 
	queue<int> espacios2;
	map<int, int> visitados;
	map<int, int>::iterator it;
	set<int>::iterator jt;

	for(it = peso.begin(); it != peso.end(); ++it) visitados[it->first] = -1;

	/* Esto es un Dijkstra que ejecuta primero un BFS para encontrar los mejores caminos hacia
	   cada alienigena, es decir, la cola de prioridad solo almacena el nodo de inicio y los demás
	   nodos alienigenas, usa un BFS aunque si encuentra un Alien usa la misma condición que el
	   algoritmo de Dijkstra para asegurarse de que siempre encuentre el camino más corto. En pocas
	   palabras se aplica del algoritmo de Dijkstra desde cada Alien que esté en el laberinto.*/

	peso[s] = total = 0;
	espacios.push(make_pair(0, s));
	while(!espacios.empty()) {
		u = espacios.top().second;
		p = espacios.top().first;
		espacios.pop();
		if(p == peso[u]) {
			total += p; // Aquí se añaden los mejores pasos encontrados.
			peso[u] = -1; // Como pueden haber más de un camino para un mismo Alien con esto se asegura que no cambie el mejor camino encontrado ni que se añadan otra vez los mismos nodos a la cola de prioridad.
			for(it = visitados.begin(); it != visitados.end(); ++it) it->second = -1;
			espacios2.push(u);
			visitados[u] = 0;
			while(!espacios2.empty()) {
				v = espacios2.front();
				espacios2.pop();

				for(jt = maze[v].begin(); jt != maze[v].end(); ++jt) {
					nodo = (*jt);
					if(visitados[nodo] == -1) {
						visitados[nodo] = visitados[v] + 1; // Se le va sumando 1 por cada nivel que suba.
						espacios2.push(nodo);
						if(traductor[nodo] == "A" && visitados[nodo] < peso[nodo]) {
							peso[nodo] = visitados[nodo];
							espacios.push(make_pair(peso[nodo], nodo));
						}
					}
				}
			}
		}
	}

	cout << total << endl;
}

int main() {
	int cases, filas, columnas, k, pos_inicialx, pos_inicialy, temp1, temp2, numero2, s;
	string temp, caracter;
	queue<pair<int, int>> puntos;
	vector<string> traductor; // Con esta estructura se sabe el id de cada símbolo del laberinto (llave primaria).
	vector<vector<string>> maze_1;
	map<int, set<int>> maze; // Se usaron conjuntos de entero para que a la hora de tener el grafo no se repitan nodos, se usa también un mapa para ahorrar las posiciones sin utilizar que habría en un vector.
	map<int, set<int>>::iterator it; 
	map<int, int> peso;

	cin >> cases;
	while(cases--) {
		cin >> columnas >> filas;
		maze_1 = vector<vector<string>>(filas, vector<string>(columnas));
		traductor = vector<string>(filas * columnas);

		k = 0;
		pos_inicialx = pos_inicialy = -1; // Con esto el algoritmo se asegura que existen nodos por los cuales moverse en el laberinto.
		cin.ignore();
		for(int i = 0; i < filas; ++i) {
			getline(cin, caracter);
			for(int j = 0; j < columnas; ++j) {
				if(caracter[j] != '#') {
					if(caracter[j] == 'S') {
						pos_inicialx = i; // Posición inicial en la fila.
						pos_inicialy = j; // Posición inicial en la columna.
					}
					traductor[k] = caracter[j]; // Se llena el vector que trae el valor original del número (símbolo).
					temp = to_string(k);
					maze_1[i][j] = temp;
				}
				else maze_1[i][j] = caracter[j];
				++k;
			}
		}

		if(pos_inicialx != -1 && pos_inicialy != -1) {

			/* Aquí se transforma la matriz de strings en un grafo con valores númericos, ya que es más fácil trabajar
			   con números que con cualquier otra cosa, entonces se mira la posición actual y de ahí se analiza tanto
			   a la izquierda como a la derecha, tanto arriba como abajo, si puede formar el grafo a partir de ese 
			   análisis, eso se logra viendo si la siguiente posición es diferente de "$" y que la posición actual también
			   lo sea, si la posición que se mira es diferente de "$" y de "#" entonces se pasa a añadirla al grafo además
			   de añadirla a la cola para procesarla, así sucesivamente con todos los nodos. */

			puntos.push(make_pair(pos_inicialx, pos_inicialy));
			while(!puntos.empty()) {
				temp1 = puntos.front().first;
				temp2 = puntos.front().second;
				puntos.pop();
				stringstream numero(maze_1[temp1][temp2]);
				numero >> numero2;
				if(temp1 == pos_inicialx && temp2 == pos_inicialy) s = numero2; // Posición inicial.
				
				// Mira derecha
				if(maze_1[temp1][temp2 + 1] != "#" && maze_1[temp1][temp2 + 1] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
					stringstream numero(maze_1[temp1][temp2 + 1]);
					numero >> k;
					maze[numero2].insert(k);
					maze[k].insert(numero2);
					puntos.push(make_pair(temp1, temp2 + 1));
				}

				// Mira izquierda
				if(maze_1[temp1][temp2 - 1] != "#" && maze_1[temp1][temp2 - 1] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
					stringstream numero(maze_1[temp1][temp2 - 1]);
					numero >> k;
					maze[numero2].insert(k);
					maze[k].insert(numero2);
					puntos.push(make_pair(temp1, temp2 - 1));
				}

				// Mira arriba
				if(maze_1[temp1 - 1][temp2] != "#" && maze_1[temp1 - 1][temp2] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
					stringstream numero(maze_1[temp1 - 1][temp2]);
					numero >> k;
					maze[numero2].insert(k);
					maze[k].insert(numero2);
					puntos.push(make_pair(temp1 - 1, temp2));
				}

				// Mira abajo
				if(maze_1[temp1 + 1][temp2] != "#" && maze_1[temp1 + 1][temp2] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
					stringstream numero(maze_1[temp1 + 1][temp2]);
					numero >> k;
					maze[numero2].insert(k);
					maze[k].insert(numero2);
					puntos.push(make_pair(temp1 + 1, temp2));
				}

				maze_1[temp1][temp2] = "$"; // Con esto se asegura el algoritmo que el nodo actual ya fue añadido al grafo, con sus nodos adyacentes.
			}

			for(it = maze.begin(); it != maze.end(); ++it) peso[it->first] = INFINITO;
			recorridoLaberinto(maze, traductor, peso, s);
		}
		else cout << 0 << endl;

		maze.clear();
		peso.clear();

	}

	return 0;
}

/* La complejidad de este algoritmo tiene varias partes, primero, en la construcción del grafo se hace en 
   O(n), luego en la partes del cálculo de la solución se hace un BFS por cada Alien es decir es O(n) * O(nlog(n)),
   donde O(nlog(n)) es el algoritmo de Dijsktra y O(n), esto al final en el peor de los casos es O(n^2), lo cual
   no lo hace un algoritmo tan eficiente como se esperaría, aún así tiene un ventaja y es que el algoritmo es fácil
   de manejar puesto a que se tiene un grafo construido y se conoce bien cada posición y lo que trae del laberinto
   original. */