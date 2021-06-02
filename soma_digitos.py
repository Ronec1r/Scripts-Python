n=int(input('Digite um número inteiro: '))
soma=0
resto=1
while resto!=0:
   soma=soma+(n%10)
   resto=n//10
   n=resto
print(soma)