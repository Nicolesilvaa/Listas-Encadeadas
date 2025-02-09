# ##################################################
# Programa de teste para uma lista encadeada
# ##################################################

import cNo
import cListaEncadeada

import sys
import random
import math

from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
def trataLinhaDeComando():
    n = 10
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
        if n < 0:
            n = 10
    return n

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    numElementos = trataLinhaDeComando()

    lista = cListaEncadeada.cLSE()

    lista.insereDado(20)
    lista.insereDado(60)
    lista.insereDado(500)
 
    print(" ----------------- Está é a lista não ordenada---------------------\n")
    if lista.buscaDado(500): 
        print("O elemento foi encontrado")

    else:
        print("Elemento não encontrado")
    

    print(str(lista))

    # Teste para lista ordenada

    listaOrdenada = cListaEncadeada.cLSE()

    listaOrdenada.insereOrd(10)
    listaOrdenada.insereOrd(20)
    listaOrdenada.insereOrd(30)
    listaOrdenada.insereOrd(40)
    listaOrdenada.insereOrd(50)
    listaOrdenada.insereOrd(60)

    print(" ----------------- Está é a lista ordenada---------------------\n")
    if listaOrdenada.buscaDado(20): 
        print("O elemento foi encontrado")

    else:
        print("Elemento não encontrado")
    
    print(str(listaOrdenada))
    

    