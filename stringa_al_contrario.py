def turn(stringa):
    if len(stringa) == 2:
        contrario = stringa[1] + stringa[0]
        return contrario

    elif len(stringa)==1:
        return stringa

    else:                           #turn (second --> ESE)  #turn (second --> SE)       #turn (first --> AGN)
        index=len(stringa)//2 #2        #3                  #ES                         #3 AG+N
                                                            #turn (first --> E)         #turn (second N) --> N
        first=stringa[:index] #AGN      #E                  #E                          #turn (first AG) --> GA
        second=stringa[index:] #ESE     #SE                                             #NGA
        return turn(second) + turn(first)
                #ESE + #NGA

if __name__=='__main__':
    print(turn("FUNZIONA!"))
