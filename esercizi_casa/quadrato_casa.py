import copy

class Quadrato:
    def __init__(self, n):
        self._soluzione=set()
        self._n=n
        self._numero_magico=self._n*(self._n*self._n+1)/2
        self.soluzioni=0

    def solve(self):
        self.soluzioni = 0
        self._soluzione.clear() #svuoto la soluzione precedente
        rimanenti=set()
        for i in range(1, (self._n**2)+1):
            rimanenti.add(i) #creo la lista con le cifre da inserire
        self._ricorsione([], self._n, rimanenti)
        self.stampa()


    def _ricorsione(self, parziale, n, rimanenti):
        #condizione terminale
        if len(parziale)==n*n: #oppure len(rimanenti == 0)
            if self.is_admissible(parziale):
                self.soluzioni += 1
                self._soluzione.add(tuple(copy.deepcopy(parziale)))

        else:
            for i in rimanenti:
                    parziale.append(i)
                    nuovi_rimanenti=copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(i) #ho usato i: lo rimuovo
                    self._ricorsione(parziale, n, nuovi_rimanenti)

                    #backtracking
                    parziale.pop()

    def is_admissible(self, parziale):
        #devo scrivere i vincoli --> faccio il controllo una volta che parziale è pieno
        #1. vincolo sulle righe
        for n_riga in range(self._n):
            inizio_intervallo=n_riga*self._n
            fine_intervallo=(n_riga+1)*self._n
            if sum(parziale[inizio_intervallo:fine_intervallo])!=self._numero_magico:
                return False

        #2. vincolo sulle colonne
        for id_col in range(self._n):
            col = parziale[id_col : (self._n-1)*self._n + id_col + 1: self._n]
            if sum(col) != self._numero_magico:
                return False

        #3. vincolo sulle diagonali
        diagonale1=parziale[:self._n**2+1:self._n+1]
        if sum(diagonale1)!=self._numero_magico:
            return False

        #controllo diagonale 2
        somma = 0
        for indice in range(self._n):
            somma += parziale[indice * self._n + (self._n - 1 - indice)]
        if somma != self._numero_magico:
            return False
        #se ho passato tutti i controlli arrivo qui!
        return True

    def stampa(self):
        for soluzione in self._soluzione: #soluzione è tipo un set di 9 elementi (1,2,6,7,8,9,3)
            print("-------------")
            for riga in range(self._n): #riga è l'indice
                print(soluzione[riga* self._n: (riga + 1) * self._n])
            print("-------------")

if __name__=="__main__":
    sq=Quadrato(3)
    sq.solve()
    print(f"soluzioni trovate: {sq.soluzioni}")
