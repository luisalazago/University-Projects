#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <queue>
#include <sstream>
#include <map>
#include <set>

#define endl '\n'

using namespace std;

void verLaberinto(vector<vector<string>>& maze_1, vector<vector<pair<int, int>>>& maze, int indice) {
	if(!indice) {
		for(int i = 0; i < maze_1.size(); ++i) {
			for(int j = 0; j < maze_1[i].size(); ++j) cout << maze_1[i][j];
			cout << endl;
		}
	}
	else {
		for(int i = 0; i < maze.size(); ++i) {
			cout << i << ": ";
			for(int j = 0; j < maze[i].size(); ++j) cout << "[" << maze[i][j].first << ", " << maze[i][j].second << "] ";
			cout  << endl; 
		}
	}
	cout << endl;
}

int main() {
	int cases, filas, columnas, k, pos_inicialx, pos_inicialy, temp1, temp2, numero2;
	string temp, caracter;
	queue<pair<int, int>> puntos;
	vector<string> traductor;
	vector<vector<string>> maze_1;
	vector<vector<pair<int, int>>> maze;

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
					traductor[k] = caracter;
					temp = to_string(k);
					maze_1[i][j] = temp;
				}
				else maze_1[i][j] = caracter[j];
				++k;
			}
		}

		verLaberinto(maze_1, maze, 0);
		cout << pos_inicialx << " " << pos_inicialy << endl;

		maze = vector<vector<pair<int, int>>>(k, vector<pair<int, int>>());
		puntos.push(make_pair(pos_inicialx, pos_inicialy));
		while(!puntos.empty()) {
			temp1 = puntos.front().first;
			temp2 = puntos.front().second;
			puntos.pop();
			stringstream numero(maze_1[temp1][temp2]);
			numero >> numero2;
			cout << numero2 << " " << maze_1[temp1][temp2] << endl;
			
			// Mira a la derecha
			if(maze_1[temp1][temp2 + 1] != "#" && maze_1[temp1][temp2 + 1] != "$" && maze_1[temp1][temp2] != "$") {
				stringstream numero(maze_1[temp1][temp2 + 1]);
				numero >> k;
				cout << k << " a" << endl;
				maze[numero2].push_back(make_pair(k, 1));
				maze[k].push_back(make_pair(numero2, 1));
				puntos.push(make_pair(temp1, temp2 + 1));
			}

			// Mira izquierda
			if(maze_1[temp1][temp2 - 1] != "#" && maze_1[temp1][temp2 - 1] != "$" && maze_1[temp1][temp2] != "$") {
				stringstream numero(maze_1[temp1][temp2 - 1]);
				numero >> k;
				cout << k << " b" << endl;
				maze[numero2].push_back(make_pair(k, 1));
				maze[k].push_back(make_pair(numero2, 1));
				puntos.push(make_pair(temp1, temp2 - 1));
			}

			// Mira arriba
			if(maze_1[temp1 - 1][temp2] != "#" && maze_1[temp1 - 1][temp2] != "$" && maze_1[temp1][temp2] != "$") {
				stringstream numero(maze_1[temp1 - 1][temp2]);
				numero >> k;
				cout << k << " c" << endl;
				maze[numero2].push_back(make_pair(k, 1));
				maze[k].push_back(make_pair(numero2, 1));
				puntos.push(make_pair(temp1 - 1, temp2));
			}

			// Mira abajo
			if(maze_1[temp1 + 1][temp2] != "#" && maze_1[temp1 + 1][temp2] != "$" && maze_1[temp1][temp2] != "$") {
				stringstream numero(maze_1[temp1 + 1][temp2]);
				numero >> k;
				cout << k << " d" << endl;
				maze[numero2].push_back(make_pair(k, 1));
				maze[k].push_back(make_pair(numero2, 1));
				puntos.push(make_pair(temp1 + 1, temp2));
			}

			maze_1[temp1][temp2] = "$";
			cout << endl;
		}

		verLaberinto(maze_1, maze, 0);
		verLaberinto(maze_1, maze, 1);

	}

	return 0;
}