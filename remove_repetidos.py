def remove_repetidos(lista_1):
    lista_2=sorted(lista_1)
    for i in lista_2:
        cont=0
        x=0
        while x<=(len(lista_2)-1):
            if i==lista_2[x]:
                cont=cont+1
                if cont>=2:
                    del lista_2[x]
            x=x+1
    return(lista_2)

