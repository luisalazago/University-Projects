#include "Trie.h"

using namespace std;

Trie::Trie(){
	
}

void Trie::agregarPatron(string p){
	arbol.agregarPatron(p);
	this->patrones.push_back(p);
}


int existeHijo(Arbol* a, char l){
	/*
		Si encuentra la letra especificada en los hijos del arbol en cuestion
		retorna la posicion de este, de lo contrario devuelve -1.
	*/
	
	int sze = (a->subArbol).size();
	
	if( sze > 0){

		for (int i = 0; i < sze; ++i){
			if( (a->subArbol[i].getElemento()) == l){

				return i;
			}
		}

	}
	return -1;
}

bool finPatron(Arbol *a){
	/*
		Retorna True si es el final de un patron, lo que significa que 
		hay un simbolo especial en el vector de arboles respectivo.
	*/

	int sze = (a->subArbol).size();
	
	if( sze > 0){

		for (int i = 0; i < sze; ++i){
			if( (a->subArbol[i].getElemento()) == '$'){
				return true;
			}
		}


	}
	return false;

}

string metadatos(Arbol *a){
	/*
		Devuelve los metadatos correspondientes.
	*/
	int sze = (a->subArbol).size();
	string meta = "";
	if( sze > 0){

		for (int i = 0; i < sze; ++i){
			if( (a->subArbol[i].getElemento()) == '$'){
				
				for (int j = 0; j < a->subArbol[i].info.size(); ++j){
					meta += a->subArbol[i].info[j];
					meta += " ";
				}
			
			}
		}


	}
	return meta;
}


vector< pair< vector<string>, int> > Trie::buscarPatronesEnCadena(string S){

	int size, counter, it, pos;

	Arbol* puntero = &arbol;
	
	vector< pair< vector<string>, int> > answer;

	string ans;

	size = S.length();
	pos = 0;
	
	for (int i = 0; i < size; ++i){
		counter = 0;
		ans = "";
		puntero = &arbol;
		pos = existeHijo(puntero, S[i]);

		it = i;
		while(pos != -1){
			counter++;
			puntero = &(puntero->subArbol[pos]);
			ans += puntero->getElemento(); 
			if( finPatron(puntero) ){

				/*Se verifica en cada añadicion de letra si es un nuevo patron, verificando con
				la funcion finPatron() */
				pair< vector<string>, int> tmp;

				tmp.first.push_back(ans);

				tmp.first.push_back( metadatos(puntero) );


				tmp.second = it - counter + 1;

				answer.push_back( tmp );

			}

			if(it + 1 < size){
				/* Se verifica que no se pase del tamaño de la palabra, para asi
					verificar que la proxima letra esté en los hijos de la letra actual
				*/
				pos = existeHijo(puntero, S[it + 1]);
				if(pos != -1){
					it++;
				}
			}
			else{
				break;
			}
		}
	}
	return answer;
}

void Trie::imprimirPatrones(){

	sort(this->patrones.begin(), this->patrones.end());
	cout << "Estos son los patrones: | ";
	for (int i = 0; i < this->patrones.size(); ++i){
		cout << this->patrones[i] << " | ";
	}
	
	cout << endl;
}

vector<string> Trie::obtenerPatrones(){
	sort(this->patrones.begin(), this->patrones.end());

	return this->patrones;
}