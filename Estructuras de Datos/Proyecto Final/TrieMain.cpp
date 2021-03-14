#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <algorithm>
#include "Arbol.h"
#include "Trie.h"

using namespace std;

int main(){
	system("cls");
	Trie a;
	string S = "ATACA";
	vector<pair< vector<string>, int>> ans;

	a.agregarPatron("AA");
	a.agregarPatron("AT");
	a.agregarPatron("C");
	a.agregarPatron("G");
	a.agregarPatron("A");


	ans = a.buscarPatronesEnCadena(S);

	for (int i = 0; i < ans.size(); ++i){
		cout << "******************************************************" << endl;
		cout << "El patron:";
		for (int j = 0; j < ans[i].first.size(); ++j){
			cout << ans[i].first[j] << " ";
		}

		cout << endl << "Empieza en la posicion: " << ans[i].second << endl;
		cout << "******************************************************" << endl;
	}

	a.imprimirPatrones();

	return 0;
}

