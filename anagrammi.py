#voglio trovare tutte le possibili permutazioni di una parola (N!)
import copy
from anyio.functools import lru_cache


class Parola:
    def __init__(self):
        self.soluzioni=list()#per non contenere duplicati

    def anagramma(self, parola:str):
        return self._ricorsione([], parola)

    def _ricorsione(self, parziale, resto):
        if len(resto) == 0:
            self.soluzioni.append(copy.deepcopy(parziale))

        else:
            for i in range (len(resto)):
                parziale.append(resto[i]) #devo farlo su righe separate sennò restituisce NoneType!
                self._ricorsione(parziale, resto[:i]+resto[i+1:])
                parziale.pop() #backtracking --> PARZIALE PRIMA DELLA RICORSIONE ERA "DO" --> ORA DIVENTA "D" E PROCEDO"


if __name__=='__main__':
    parola=("dog")
    an=Parola()
    an.anagramma(parola)
    print(an.soluzioni)
    print(len(an.soluzioni)) #per controllare che sia N!