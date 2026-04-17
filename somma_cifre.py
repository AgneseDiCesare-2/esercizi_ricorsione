def somma_cifre(n:str):
    l=len(n) #numero cifre di n
    if l==1:
        return n
    else:
        somma=int(n[0])+int(n[1]) #3
        nuovo= str(somma) + n[2:]  #concateno la somma con il resto del numero (come stringa) --> #334
        #print (nuovo)
        return somma_cifre(nuovo)

if __name__=='__main__':
    print(somma_cifre("12345"))