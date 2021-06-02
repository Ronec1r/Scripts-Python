n=int(input('Digite um número inteiro: '))
cont=0
resto=1
if n==0:
    print('não')
else:
    while resto!=0: 
        num=n%10
        resto=n//10
        num2=resto%10
        if (num==num2):
            cont=cont+1
        n=resto
    if cont>=1:
        print('sim')
    else:
        print('não')