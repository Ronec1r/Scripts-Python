i=int(input('Digite um número inteiro: '))
if (i==1):
    print('Não primo')
else:
    if (i%2==0 and i!=2) or (i%3==0 and i!=3) or (i%5==0 and i!=5) or (i%7==0 and i!=7):
        print('Não Primo')
    else:
        print('Primo')