#abbiamo una scacchiera 4x4 --> come metto le 4 regine?
import copy


class Scacchiera:
    def __init__(self, ):
        self.num_soluzioni=0
        self.num_chimate=0
        self._soluzioni=[]

    def solve(self, n):
        self._soluzioni=[] #NB!
        self._ricorsione([], n)


    def _ricorsione(self, parziale, n):
        self.num_chimate+=1
        if len(parziale)==n:
            if self.is_nuova_soluzione(parziale):
            #if self._is_soluzione(parziale): diventa superfluo se uso step_valid
                self.num_soluzioni += 1
                self._soluzioni.append(copy.deepcopy(parziale)) #su parziale sto facendo pop, quindi considero la copia!

        else:
           for riga in range(n):
               for colonna in range(n):
                    nuova_regina=[riga, colonna]
                    if self._step_is_valid(nuova_regina, parziale):
                        #aggiungiamo alla soluzione parziale
                        parziale.append(nuova_regina)

                        #andiamo avanti con la ricorsione
                        self._ricorsione(parziale, n)

                        #backtracking --> molto importante (SEMPRE)
                        parziale.pop() #tolgo l'ultimo elemento che ho --> si usa per esplorare più rami di soluzione
                        #dopo che ho trovato una soluzione (e stampata su una riga in output), elimino l'ultimo elemento e ricomincio.

    #controlla se la nuova regina da inserire sia ammissibile rispetto alla soluzione parziale costruita fino'ora

    def _step_is_valid(self, nuova_regina, parziale) -> bool:
        for regina in parziale:
            if not self._is_admissible(nuova_regina, regina):
                return False
        return True

    def _is_admissible(self, regina1, regina2) -> bool:
        #verifico la riga, la colonna e le due diagonali
        if (regina1[0] == regina2[0] or regina1[1] == regina2[1] or (regina1[0]-regina1[1]==regina2[0]-regina2[1]) or (regina1[0]+regina1[1]==regina2[0]+regina2[1])) :
            return False
        else:
            return True

    #vedo se la configurazione è già presente
    def is_nuova_soluzione(self, soluzione_potenziale):
        n=len(soluzione_potenziale)
        for soluzione in self._soluzioni:
            counter=0
            for regina in soluzione_potenziale:
                if regina in soluzione:
                    counter+=1

            if counter==n:
                return False #soluzione già presente
        return True

    #def _is_soluzione(self, soluzione_possible) -> bool:
    #   for i in range(len(soluzione_possible)-1):
    #        for j in range(i+1, len(soluzione_possible)):
    #            if not self._is_admissible(soluzione_possible[i], soluzione_possible[j]):
    #                return False
    #    return True

if __name__=="__main__":
    nreg=Scacchiera()
    nreg.solve(4)
    print(f"numero chiamate: {nreg.num_chimate}")
    print(f"numero soluzioni: {nreg.num_soluzioni}")
    print(nreg._soluzioni)