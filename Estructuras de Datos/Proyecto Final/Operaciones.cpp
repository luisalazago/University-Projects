#include "Operaciones.h"

using namespace std;

Operaciones::Operaciones(){

}

vector<int> Operaciones::RetornarFuncionFallo(){
	return fallo;
}

void Operaciones::CalcularFuncionFallo(string patron){
	
	vector<int> f;
	int index = 0, count = 0;
	f.push_back(0);

	for (int i = 1; i < patron.length(); ++i){
		
		if(patron[i] == patron[index]){
			f.push_back(index + 1);
			index++;
		}else{
			index = 0;
			f.push_back(0);
		}
	}
	fallo = f;

}

vector<int> Operaciones::BuscarPatronEnCadena(string cadena, string patron){

	vector<int> result;
	int i = 0, j = 0, itemp = 0, h = 0;

	while(i < cadena.length()){
		if(cadena[i] == patron[0]){
			for (h = 0, itemp = i; h < patron.length() && itemp < cadena.length(); ++h, ++itemp){
				if(cadena[itemp] != patron[h]){
					i += fallo[h];
					break;
				}
			}
			if(h == patron.length()){
				result.push_back(i);
			}
			i++;
		}
		else{
			i++;
		}
	}
	return result;
}

vector<int> Operaciones::busquedaIngenua(string cadena, string patron){
	int j, i, ver;
	vector<int> sol;
	for(i = 0; i <= cadena.size() - patron.size(); i++){
		ver = 1;
		for(j = 0; j < patron.size() && ver; j++){
			if(patron[j] != cadena[i + j]) ver = 0;
		}
		
		if(ver) sol.push_back(i);
	}
	return sol;
}