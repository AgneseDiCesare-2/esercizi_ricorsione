from time import time


class Fibonacci:
    def __init__(self):
        self.cache={0: 0, 1: 1} #due soluzioni le so già
        pass

    def calcola_elemento_cache(self, n):
        #funzione che salve le sequenze calcolate in memoria
        #se ho già la soluzione per questo n --> la prendo dalla cache
        if n in self.cache.keys():
            return self.cache[n] #soluzione
        else:
            nuovo=self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2)
            self.cache[n]=nuovo #aggiungo al dizionario
            return nuovo

    def calcola_elemento(self, n):
        #caso terminale sdoppiato
        if n==0:
            return 0
        elif n==1:
            return 1

        #caso non terminale
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

if __name__=='__main__':
    fib=Fibonacci()
    start_time=time()
    print(fib.calcola_elemento_cache(121))
    end_time=time()
    print(f"{end_time-start_time} seconds") #impiega tanto tempo se non uso la cache:-(
    #guadagno molto tempo se uso la cache :-)