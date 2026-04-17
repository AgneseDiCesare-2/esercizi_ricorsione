def dichotomic(input, val):
    if len(input)==1:
        if input[0]==val:
            return True
        else:
            return False

    else:
        index=len(input)//2
        return dichotomic(input[:index],val) or dichotomic(input[index:],val) #uso or--> se uno dei due contiene val restituisce True

if __name__=='__main__':
    sequenza=[1,2,3,4,5,6,7,8,9,10]
    print(dichotomic(sequenza, 4))
    print(dichotomic(sequenza, 11))