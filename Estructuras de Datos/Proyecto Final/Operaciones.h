#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

#ifndef __Operaciones_H
#define __Operaciones_H

class Operaciones{

  private:
    vector<int> fallo;

  public:
    Operaciones();

    void CalcularFuncionFallo(string patron);

    vector<int> BuscarPatronEnCadena(string cadena, string patron);

    vector<int> busquedaIngenua(string cadena, string patron);
    
    vector<int> RetornarFuncionFallo();

    ~Operaciones(); 
};

#endif