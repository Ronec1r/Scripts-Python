n=int(input(': '))
fator=2
while n%fator!=0:   
    fator=fator+1
if n==fator and n!=1:
    print('primo')
else:
    print('não primo')
