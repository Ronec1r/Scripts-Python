def maximo(n,m,o):
    if ((n>m) or (n==m)) and ((n>o) or (n==o)):
        return(n)
    elif (m>n) and (m>o):
        return(m)
    else:
        return(o)