def maior_elemento(lista):
    maior_numero=lista[0]
    for i in lista:
        if i>maior_numero:
            maior_numero=i
    return maior_numero 

    