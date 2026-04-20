#voglio trovare tutte le possibili permutazioni di una parola (N!)
import copy

from anyio.functools import lru_cache


class Parola:
    def __init__(self):
        self.soluzioni=set() #per non contenere duplicati

    def anagramma(self, parola: str):
        self._ricorsione("", parola)

    @lru_cache(maxsize=None) #una volta che vede ... ?
    def _ricorsione(self, inizio, resto):
        if len(resto)==0:
            self.soluzioni.add(copy.deepcopy(inizio)) #meglio usare questa lista al posto di quella che modifico
        else:
            n=len(resto)
            for i in range(n):
                self._ricorsione(inizio + resto[i], resto[:i] + resto[i+1:])

if __name__=='__main__':
    parola=("dog")
    an=Parola()
    an.anagramma(parola)
    print(an.soluzioni)
    print(len(an.soluzioni)) #per controllare che sia N!