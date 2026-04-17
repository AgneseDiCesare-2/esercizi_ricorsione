def palindromo(s: str):
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1]:
            return palindromo(s[1:-1]) #considero dal secondo carattere al penultimo.
        else:
            return False

if __name__=="__main__":
    parola="ingegni"
    print(palindromo(parola))

