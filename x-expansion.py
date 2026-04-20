class XExpansion:
    def __init__(self):
        self.soluzioni=[]

    def calcola(self, input):
        self._ricorsione("", input)

    #paziale è la soluzione parziale
    #rimanenti sono il resto dei caratteri da esaminare

    #NB: copy.deepcoy(lista) --> duplica tutti gli elementi di una lista
    #si usa quando devo modicare la lista

    def _ricorsione(self, parziale: str, rimanenti: str):
        #caso terminale
        if len (rimanenti) == 0:
            self.soluzioni.append(parziale)
        else:
            if rimanenti[0] == "X":
               self._ricorsione(parziale+'0', rimanenti[1:])
               self._ricorsione(parziale + '1', rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])

if __name__ == "__main__":
    sequenza="01X0X"
    xexp = XExpansion()
    xexp.calcola(sequenza)
    print(xexp.soluzioni)