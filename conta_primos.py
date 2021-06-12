def éprimo(k):
    fator=2
    if k==2:
        return True
    while k%fator!=0:
        fator=fator+1
    if k==fator and k!=1:
        return True
    else:
        return False

def n_primos(n):
    cont=0
    while n>=2:
        if éprimo(n):
            cont=cont+1
        n=n-1
    return(cont)
