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

void verLaberinto(vector<vector<string>>& maze_1, map<int, set<pair<int, int>>>& maze, int indice) {
	if(!indice) {
		for(int i = 0; i < maze_1.size(); ++i) {
			for(int j = 0; j < maze_1[i].size(); ++j) cout << maze_1[i][j];
			cout << endl;
		}
	}
	else {
		map<int, set<pair<int, int>>>::iterator it;
		set<pair<int, int>>::iterator jt;
		for(it = maze.begin(); it != maze.end(); ++it) {
			cout << "[" << it->first << "] = ";
			for(jt = it->second.begin(); jt != it->second.end(); ++jt) cout << "(" << (*jt).first << ", " << (*jt).second << ") ";
			cout << endl;
		}
	}
	cout << endl;
}

void recorridoLaberinto(map<int, set<pair<int, int>>>& maze, vector<string>& traductor, map<int, int>& peso, int s) {
	int u, p, pesoA, v, total;
	vector<int> sumadores;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> espacios;
	set<pair<int, int>>::iterator jt;
	map<int, bool> visitados, pred;
	map<int, set<pair<int, int>>>::iterator it;

	for(it = maze.begin(); it != maze.end(); ++it) {
		visitados[it->first] = false;
		pred[it->first] = -1;
	}

	peso[s] = 0;
	espacios.push(make_pair(0, s));
	while(!espacios.empty()) {
		u = espacios.top().second;
		p = espacios.top().first;
		visitados[u] = true;
		espacios.pop();
		cout << "Nodo [" << u << "]: ";

		if(p == peso[u]) {
			for(jt = maze[u].begin(); jt != maze[u].end(); ++jt) {
				v = (*jt).first;
				pesoA = (*jt).second;
				cout << "(" << v << ", " << pesoA + p;
				if(visitados[v]) cout << ", verdadero) ";
				else cout << ", falso) ";

				if(!visitados[v] && pesoA + p < peso[v]) {
					peso[v] = pesoA + p;
					pred[v] = u;

					if(traductor[v] == "A") {
						cout << "es A ";
						sumadores.push_back(peso[v]);
						visitados[u] = false;
						peso[v] = 0;
					}
					espacios.push(make_pair(peso[v], v));
				}
			}
		}
		cout << endl;
	}

	total = 0;
	for(int i = 0; i < sumadores.size(); ++i) total += sumadores[i];
	cout << total << endl;
	cout << endl;
}

int main() {
	int cases, filas, columnas, k, pos_inicialx, pos_inicialy, temp1, temp2, numero2, s;
	string temp, caracter;
	queue<pair<int, int>> puntos;
	vector<string> traductor; // Con esta estructura se sabe el id de cada símbolo del laberinto (llave primaria).
	vector<vector<string>> maze_1;
	map<int, set<pair<int, int>>> maze; // Se usaron conjuntos de parejas para que a la hora de tener el grafo no se repitan parejas, se usa también un mapa para ahorrar las posiciones sin utilizar que habría en un vector.
	map<int, set<pair<int, int>>>::iterator it;
	map<int, int> peso;

	cin >> cases;
	while(cases--) {
		cin >> columnas >> filas;
		maze_1 = vector<vector<string>>(filas, vector<string>(columnas));
		traductor = vector<string>(filas * columnas);

		k = 0;
		cin.ignore();
		for(int i = 0; i < filas; ++i) {
			getline(cin, caracter);
			for(int j = 0; j < columnas; ++j) {
				if(caracter[j] != '#') {
					if(caracter[j] == 'S') {
						pos_inicialx = i;
						pos_inicialy = j;
					}
					traductor[k] = caracter[j];
					temp = to_string(k);
					maze_1[i][j] = temp;
				}
				else maze_1[i][j] = caracter[j];
				++k;
			}
		}

		verLaberinto(maze_1, maze, 0);
		cout << pos_inicialx << " " << pos_inicialy << endl;

		puntos.push(make_pair(pos_inicialx, pos_inicialy));
		while(!puntos.empty()) {
			temp1 = puntos.front().first;
			temp2 = puntos.front().second;
			puntos.pop();
			stringstream numero(maze_1[temp1][temp2]);
			numero >> numero2;
			// cout << "-" << numero2 << ": ";
			if(temp1 == pos_inicialx && temp2 == pos_inicialy) s = numero2;
			
			// Mira a la derecha
			if(maze_1[temp1][temp2 + 1] != "#" && maze_1[temp1][temp2 + 1] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
				stringstream numero(maze_1[temp1][temp2 + 1]);
				numero >> k;
				// cout << "derecha " << k << ", ";
				maze[numero2].insert(make_pair(k, 1));
				maze[k].insert(make_pair(numero2, 1));
				puntos.push(make_pair(temp1, temp2 + 1));
			}

			// Mira izquierda
			if(maze_1[temp1][temp2 - 1] != "#" && maze_1[temp1][temp2 - 1] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
				stringstream numero(maze_1[temp1][temp2 - 1]);
				numero >> k;
				// cout << "izquierda " << k << ", ";
				maze[numero2].insert(make_pair(k, 1));
				maze[k].insert(make_pair(numero2, 1));
				puntos.push(make_pair(temp1, temp2 - 1));
			}

			// Mira arriba
			if(maze_1[temp1 - 1][temp2] != "#" && maze_1[temp1 - 1][temp2] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
				stringstream numero(maze_1[temp1 - 1][temp2]);
				numero >> k;
				// cout << "arriba " << k << ", ";
				maze[numero2].insert(make_pair(k, 1));
				maze[k].insert(make_pair(numero2, 1));
				puntos.push(make_pair(temp1 - 1, temp2));
			}

			// Mira abajo
			if(maze_1[temp1 + 1][temp2] != "#" && maze_1[temp1 + 1][temp2] != "$" && maze_1[temp1][temp2] != "$" && maze_1[temp1][temp2] != "#") {
				stringstream numero(maze_1[temp1 + 1][temp2]);
				numero >> k;
				// cout << "abajo " << k << ", ";
				maze[numero2].insert(make_pair(k, 1));
				maze[k].insert(make_pair(numero2, 1));
				puntos.push(make_pair(temp1 + 1, temp2));
			}

			// cout << endl;
			maze_1[temp1][temp2] = "$";
		}

		// verLaberinto(maze_1, maze, 0);
		verLaberinto(maze_1, maze, 1);

		for(it = maze.begin(); it != maze.end(); ++it) peso[it->first] = INFINITO;
		recorridoLaberinto(maze, traductor, peso, s);

		maze.clear();
		peso.clear();
	}

	return 0;
}