def é_hipotenusa(k):
    i=1
    j=1
    while i<=k:
        j=1
        while j<=k:
            if k**2==(i**2)+(j**2):
                return True
            else:
                j=j+1
        i=i+1
    return False

def soma_hipotenusas(n):
    soma=0
    while n>=1:
        if é_hipotenusa(n):
            soma=soma+n
        n=n-1
    return(soma)
