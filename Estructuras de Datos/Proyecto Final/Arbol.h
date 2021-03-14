#ifndef _ARB_
#define _ARB_
#include <iostream>
#include <vector>
#include <string>

//Pre orden busqueda por profundidad
using namespace std;

class Arbol{
	private:
		char elemento;
		int profundidad;
		int ramas;
	
	public:
		/*Atributos*/
		vector<Arbol> subArbol;
		vector<string> info;
		
		/*Constructoras*/
		Arbol(); //Vacia
		Arbol(char c); //Para añadir el dato que va en la raiz
		Arbol(string des_tec, char iden, string porcentaje); //Para añadir la informacion alfinal de la rama
		
		/*Contadores*/
		int maximaProfundidad();
		int contarRamas();
		
		/*Impresion*/
		void agregarPatron(string patron);
		void imprimirPreOrden();
		void imprimirPostOrden();
		void imprimirBusquedaAnchura();
		void imprimirBusquedaProfundidad();
		
		/*Información*/
		string listarPreOrden();		
		string listarPostOrden();
		string listarBusquedaAnchura();
		string listarBusquedaProfundidad();
		
		/*Ver elementos*/
		char getElemento();
		
		/*Modificar atributos*/
		void setRamas(int n);
		void setProfundidad(int n);
};

#endif

