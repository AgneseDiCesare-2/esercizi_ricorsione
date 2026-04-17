def massimo(lista):
    if len(lista) == 1:
        return lista[0]

    else:
        max = lista[0]
        print (lista)
        if lista[1]>max:
            return massimo(lista[1:])
        else:
            lista.pop(1)
            return massimo(lista)

if __name__=='__main__':
    print(massimo([1,3,2,5,4,6,7,8,9,2,1]))