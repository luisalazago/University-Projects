#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <algorithm>
#include "Arbol.h"

using namespace std;

#ifndef __Trie_H
#define __Trie_H

class Trie{

  private:
  	/*Atributos*/
    Arbol arbol;
    vector<string> patrones;


  public:
  	/*Constructor*/
    Trie();

    /*Modificar atributos*/
    void agregarPatron(string p);
    
    /*Información*/
    vector< pair< vector<string>, int> > buscarPatronesEnCadena(string S);
    void imprimirPatrones();
    vector<string> obtenerPatrones();

};

#endif