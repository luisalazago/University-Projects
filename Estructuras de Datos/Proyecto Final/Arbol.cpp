#include "Arbol.h"

using namespace std;

/*Funciones de ayuda*/
void devolver(vector<Arbol> subA, string* r, int j){
	if(j == 0){
		for(int i = 0; i < subA.size(); i++){
			if(subA[i].getElemento() != '$') (*r) += ',';
			(*r) += '[';
			(*r) += subA[i].getElemento();
			if(subA[i].getElemento() != '$') (*r) += ',';
					
			devolver(subA[i].subArbol, r, j);
		}
		(*r) += ']';
	}
	
	else{
		for(int i = 0; i < subA.size(); i++){
			(*r) += ", ";
			(*r) += subA[i].getElemento();	
			devolver(subA[i].subArbol, r, j);
		}
	}
}

void buscarAnchura(vector<Arbol> temporal1, vector<vector<char>>& temporal2) {
	int len;
	for(int i = 0; i < temporal1.size(); i++) {
		len = temporal1[i].maximaProfundidad(); // Esto guarda la profundidad en la que está cada elemento.
		temporal2[len].push_back(temporal1[i].getElemento());
		buscarAnchura(temporal1[i].subArbol, temporal2);
	}
}

/*Constructora vacia para la creación de la raiz*/
Arbol::Arbol(){
	elemento = 'R';
	subArbol.clear();
	info.clear();
	profundidad = ramas = 0;
}

/*Constructora con un char para la creación de un nodo*/
Arbol::Arbol(char c){
	elemento = c;
	subArbol.clear();
	info.clear();
	profundidad = ramas = 0;
}

/*Constructora con la información del ultimo nodo de una rama, es
  decir el caracter especial*/
Arbol::Arbol(string des_tec, char iden, string porcentaje){
	elemento = iden;
	subArbol.clear();
	info.clear();
	info.push_back(des_tec);
	info.push_back(porcentaje);
	profundidad = ramas = 0;
}

/*Procedimientos para setear los atributos*/
void Arbol::setProfundidad(int n){
	profundidad = n;
}

void Arbol::setRamas(int n){
	ramas = n;
}

/*Función para conocer el valor del nodo*/
char Arbol::getElemento(){
	return elemento;
}

/*Funcion que me dice la maxima profundidad*/
int Arbol::maximaProfundidad(){
	return profundidad;	
}

/*Funcion que me dice la cantidad de ramas del arbol*/
int Arbol::contarRamas(){
	return ramas;
}

/*Procedimiento que crea una nueva rama en el arbol*/
void Arbol::agregarPatron(string p){
	//Datos para conocer los datos
	string copia = p;
	vector<Arbol> *listado = &subArbol;
	vector<Arbol> *anterior = &subArbol;
	bool ver = true;
	int i = 0, n = 1, j = 0;
	if((*listado).size() == 0) ver = false;
	
	//Ciclo de busqueda, es decir busca en que punto en patron difiere con una rama que el arbol ya tiene
	while(ver){
		
		//Condicional que me dice cuando el patron se asemeja al valor buscado y en la misma profundidad
		if((*listado)[i].getElemento() == p[0]){
			
			p.erase(p.begin());
			anterior = listado;
			listado = &(*listado)[i].subArbol;
			j = i;
			i = 0;
			n++;
		}

		else i++;
		
		//Condicional que me dice cuando no puede seguir la rama para empezar a construir una nueva
		if(i == (*listado).size()){
			ver = false;
			// Le asigno la cantidad de ramas que tiene el nodo actual
			if(n != 1 ) (*anterior)[j].setRamas(i);
			
			else ramas = subArbol.size();
		} 
	}
	
	ver = true;
	
	// Ciclo que empieza a agregar los nodos
	while(ver){
		//condicional me dice cuando hay que agregar el listado de los caracteres especiales y la información. Mejorar para ocupar el tercer costructor
		if(p.size() == 0){

			string des_tec, porcentaje;
			cout << "--------------------------------------------" << endl;
			cout << "INGRESE METADATOS PARA: " << copia << endl;
			cout << "1) Descripcion tecnica: ";
			cin >> des_tec;
			cout << endl << "2) Porcentaje: " << endl;
			cin >> porcentaje;
			cout << "--------------------------------------------" << endl;
			Arbol a(des_tec, '$', porcentaje);	
			

			a.setRamas(0);
			a.setProfundidad(n);
			ver = false;
			(*listado).push_back(a);
			profundidad = profundidad < n ? n : profundidad;
		} 
		
		//Condicional para agregar los distintos nodos
		else{
			Arbol a(p[0]);
			a.setRamas(1);
			a.setProfundidad(n);
			j = 0;
			p.erase(p.begin());
			(*listado).push_back(a);
		}
		
		//Reservo memoria para poder almacenar los nuevos nodos en el arbol original
		n++;
		vector<Arbol> *temp = new vector<Arbol>;
		temp = &(*listado); //al nuevo espacio de memoria reservado le paso la direción de memoria del vector de Aroles del nodo Actual
		listado = &(*listado)[(*listado).size() - 1].subArbol; //Me muevo al nuevo listado de arboles, es decir del nodo que yo agregue
	}
}

/*Funciones que me devuelven los procedimientos de una busqueda sobre el arbol*/
string Arbol::listarPreOrden(){
	string r = "";
	r += '[';
	r += elemento;
	devolver(subArbol, &r, 0);
	return r;
}

string Arbol::listarBusquedaProfundidad(){
	string r = "";
	r += elemento;
	devolver(subArbol, &r, 1);
	return r;
}

string Arbol::listarBusquedaAnchura() {
	string cadena = "";
	cadena += elemento;
	cadena += ", ";
	vector<vector<char>> temp2(profundidad + 1); // Contando el nodo Raiz
	buscarAnchura(subArbol, temp2);
	for(int i = 0; i < temp2.size(); i++) {
		for(int j = 0; j < temp2[i].size(); j++) {
			cadena += temp2[i][j];
			cadena += ", ";
		}
	}
	cadena[cadena.size() - 1] = ' ';
	cadena[cadena.size() - 2] = ' ';
	return cadena;
}

/*Impresion*/
void Arbol::imprimirPreOrden(){
	cout << this->listarPreOrden() << endl;
}

void Arbol::imprimirBusquedaProfundidad(){
	cout << this->listarBusquedaProfundidad() << endl;
}

void Arbol::imprimirBusquedaAnchura() {
	cout << this->listarBusquedaAnchura() << endl;
}
