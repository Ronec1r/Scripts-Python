def eprimo(k):
    if (k%2==0 and k!=2) or (k%3==0 and k!=3) or (k%5==0 and k!=5) or (k%7==0 and k!=7) or (k%31==0 and k!=31):
        return(False)
    else:
        return(True)



def maior_primo(k):
    if eprimo(k)==True:
        return(k)
    else:
        while eprimo(k)!=True:
            k=k-1
            eprimo(k)
            if eprimo(k)==True:
                return(k)


