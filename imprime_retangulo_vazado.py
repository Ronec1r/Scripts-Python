largura=int(input('Informe a largura do retângulo: '))
altura=int(input('Informe a altura do retângulo: '))
largura_2=largura
if altura==1:
    while largura_2>1:
        print('#',end='')
        largura_2=largura_2-1
    print('#')
else:
    while largura_2>1:
        print('#',end='')
        largura_2=largura_2-1
    print('#')
    while altura>2:
        largura_2=largura
        print('#',end='')
        while largura_2>2:
            print(' ',end='')
            largura_2=largura_2-1
        print('#')
        altura=altura-1
    largura_2=largura
    while largura_2>1:
        print('#',end='')
        largura_2=largura_2-1
    print('#')
