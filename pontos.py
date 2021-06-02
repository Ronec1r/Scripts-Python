from math import sqrt
x1=float(input('Digite o valor de x no primeiro ponto: '))
y1=float(input('Digite o valor de y no primeiro ponto: '))
x2=float(input('Digite o valor de x no segundo ponto: '))
y2=float(input('Digite o valor de y no segundo ponto: '))

distancia=sqrt((x1-x2)**2 + (y1-y2)**2)

if (distancia>=10):
    print('longe')
else:
    print('perto')