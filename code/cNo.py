# ##################################################
# Classe nó de uma Lista Simplesmente Encadeada
# ##################################################

class cNo:

# *******************************************************
# *******************************************************
    def __init__(self, dado=0):

        self._dado = dado
        self._prox = None

# *******************************************************
# *******************************************************
    def __str__(self):

        outStr = ""

        if self:
            outStr +=  "+==================+======+==================+\n"
            outStr += f'| {hex(id(self)):16} | {self._dado:4} | {hex(id(self._prox)):16} | \n'
            outStr +=  "+==================+======+==================+\n"
            outStr +=  "                                  |   \n"
            outStr +=  "                                  |   \n"
            if self._prox:
                outStr +=  "           +----------------------+   \n"
                outStr +=  "           |            \n"
                outStr +=  "           V            \n"
            else:
                outStr +=  "                                 ===   \n"
        
        return outStr

# *******************************************************
# *******************************************************
    def setDado(self, dado):
        self._dado = dado

        
# *******************************************************
# *******************************************************
    def setProx(self, prox):

        if type(prox) == cNo:
            self._prox = prox

        else:
            self._prox = None

# *******************************************************
# *******************************************************
    def getDado(self):
        return self._dado

# *******************************************************
# *******************************************************
    def getProx(self):
        return self._prox 

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    no      = cNo()   
    outroNo = cNo(20)

    print(str(no))
    print(str(outroNo))

    no.setDado(100)
    no._dado = 200
    no.setProx(outroNo)
        
    print(str(no))
    print(str(outroNo))

