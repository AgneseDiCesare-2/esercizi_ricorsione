def quicksort(sequenza):
    if len(sequenza) <=1:
        return sequenza
    else:
        pivot=sequenza[0] #scelgo un elemento arbitrario, comodo il primo
        #divido la sequenza seconod il pivot
        sequenza_smaller=[]
        sequenza_pivot=[]
        sequenza_larger=[]

        for i in sequenza:
            if i < pivot:
                sequenza_smaller.append(i)
            elif i==pivot:
                sequenza_pivot.append(i)
            else:
                sequenza_larger.append(i)

        return quicksort(sequenza_smaller) + sequenza_pivot + quicksort(sequenza_larger) #IMPORTANTE!

if __name__=='__main__':
    sequenza=[6,7,2,3,0,10,4,6,1,2,14,67,1]
    print(quicksort(sequenza))