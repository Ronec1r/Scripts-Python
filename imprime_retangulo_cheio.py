largura=int(input('Informe a largura do retângulo: '))
altura=int(input('Informe a altura do retângulo: '))
while altura>=1:
    largura_2=largura
    while largura_2>1:
        print('#',end='')
        largura_2=largura_2-1
    print('#')
    altura=altura-1

