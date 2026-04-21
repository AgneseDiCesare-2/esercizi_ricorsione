class Scacchiera:
    def __init__(self):
        self.n_chiamate=0
        self.n_soluzioni=0


    #n è la dimensione della scacchiera (nxn)
    def definisci_formazioni(self, n:int):
        return self._ricorsione([], n)

    @staticmethod
    def _is_ammissible(regina: tuple, parziale:list):
        for soluzione in parziale:
            if (soluzione[0] == regina[0]) or soluzione[1]==regina[1] or (regina[0] - regina[1] == soluzione[0] - soluzione[1]) or (regina[0] + regina[1] == soluzione[0] + soluzione[1]):
                return False
        return True

    #in parziale aggiungo man mano la soluzione parziale (riga, colonna)
    def _ricorsione(self, parziale, n):
        self.n_chiamate += 1

        if len(parziale)==n:
            self.n_soluzioni += 1
            print(parziale)

        else:
            for i in range (n):
                for j in range (n):
                    nuova_regina=(i, j) #ogni regina è una tupla (riga, colonna)
                    #parziale è una lista di tuple: [(i1, j1), (i2, j2) ...]
                    if self._is_ammissible(nuova_regina, parziale): #parziale prima di aggiungere eventuale regina
                        parziale.append(nuova_regina)

                        self._ricorsione(parziale, n)

                        #backtracking
                        parziale.pop() #--> voglio esplorare tutte le soluzioni

if __name__ == "__main__":
    exp=Scacchiera()
    (exp.definisci_formazioni(4))
    print(exp.n_chiamate)
    print(exp.n_soluzioni)
