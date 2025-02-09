# ############################################################
# Classe que implementa uma Lista Simplesmente Encadeada - LSE
# ############################################################

import cNo

# *******************************************************
# ***                                                 ***
# *******************************************************

class cLSE:

# *******************************************************
# ***                                                 ***
# *******************************************************

    def __init__(self):
        self._inicio     = None
        self._numElems   = 0

# *******************************************************
# ***                                                 ***
# *******************************************************
    def getTamanho(self):
        return self._numElems

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __str__(self):

        outStr = ""

        if self._inicio == None:        
            outStr += "=====================\n"
            outStr += "|   LISTA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            
            noCor = self._inicio
            while noCor != None:
      
                print(noCor)
                noCor = noCor.getProx()

        return outStr

# *******************************************************
# ***                                                 ***
# *******************************************************
    def insereDado(self,n):

        novoNo = cNo.cNo(n)

        if self._inicio == None:
            self._inicio = novoNo

        else:

            noCor = self._inicio
            while noCor.getProx() != None:
                noCor = noCor.getProx()

            noCor.setProx(novoNo)

            self._numElems += 1

        return True
    
    #Rascunho
    def insereOrd(self,n):

        novoNo = cNo.cNo(n)

        if self._inicio == None or self._inicio.getDado() > n:
            novoNo.setProx(self._inicio)
            self._inicio = novoNo
            return True

        noCor = self._inicio

        while noCor.getProx() != None and noCor.getProx().getDado() <= n:
            noCor = noCor.getProx()
           
        novoNo.setProx(noCor.getProx())
        noCor.setProx(novoNo)
        
        return True

# *******************************************************
# ***                                                 ***
# *******************************************************
    def buscaDado(self, busca):

        if self._inicio == None:
            return False
        
        noCor = self._inicio
        while noCor != None:
            if noCor.getDado()  == busca:
                return True
            noCor = noCor.getProx()
            
        return False

# *******************************************************
# ***                                                 ***
# *******************************************************
    def removeDado(self, elemento):

        noCor = self._inicio
        anterior = None

        if noCor == None:
            return False
        
        while noCor != None and noCor.getDado() != elemento:

            anterior = noCor
            noCor = noCor.getProx()

        if noCor == None:
            return False

        if anterior == None:
            self._inicio =  noCor.getProx()
        else:
            anterior.setProx(noCor.getProx())

        self._numElems -= 1
        del noCor

        return True
    

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    lista = cLSE()

    print(lista)

    lista.insereDado(40)
    lista.insereDado(10)
    lista.insereDado(78)

    print(lista)

    if lista.buscaDado(10):
        print("Busca com sucesso")
    else:
        print("Busca sem sucesso")

    if lista.removeDado(78):
        print("Remoção com sucesso")
    else:
        print("Remoção sem sucesso")

    print(lista)
