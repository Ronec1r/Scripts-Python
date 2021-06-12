lista_1=[]
num=1
while num!=0:
    num=int(input('Digite um número: '))
    if num!=0:
        lista_1.append(num)

i=len(lista_1)-1

while i>=0:
    print(lista_1[i])
    i=i-1

