def count_leaf_nodes(input_list):
    if len(input_list)==0:
        return 0
    else:
        counter=0
        for element in input_list:
            #controlla se l'elemento è una lsita
            if type(element)==list:
                counter+=count_leaf_nodes(element)
            else:
                counter += 1 #se non è una lista è una stringa
        return counter

if __name__=="__main__":
    names=['Adam', ['Bob', ['Chet', 'Cat']], 'Barb', 'Sam', ['Jack', 'Barbarossa']]
    print(count_leaf_nodes(names))