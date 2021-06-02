def fatorial(num):
    fat=1
    while (num>=1):
        fat=fat*num
        num=num-1
    return fat

def binomio():
    n=int(input('Digite o valor de n: '))
    k=int(input('Digite o valor de k: '))
    bin=fatorial(n)/(fatorial(k)*fatorial(n-k))
    print('O resultado foi igual a:', bin)

binomio()