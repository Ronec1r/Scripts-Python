print('Escolha o que quer fazer de acordo com a tabela a seguir: \n')
print('a.Calcular a soma de 15 números inteiros')
print('b.Calcular a média de 10 números inteiros')
print('c.Calcular o produto de 10 números inteiros')
print('d.Ler 15 números, mostrar o produto dos ímpares e a soma dos pares')
print('e.Ler o sexo de 10 pessoas e mostrar quantas são Masculinas e quantas são femininas')
print('f.Ler a idade de N pessoas e mostrar a maior e a menor')
print('g.Ler a idade de N pessoas e mostrar quantas são crianças, adolescentes, adultos e idodos')
print('s.Sair')
escolha=input(':')
while escolha!='s':
    if escolha=='a':
        i=1
        soma=0
        while i<=15:
            num=int(input('Digite o número: '))
            soma=soma+num
            i=i+1
        print(soma)
    elif escolha=='b':
        i=1
        soma=0
        while i<=10:
            num=int(input('Digite o número: '))
            soma=soma+num
            i=i+1
        media=soma/10
        print(media)  
    elif escolha=='c':
        i=1
        produto=1
        while i<=10:
            num=int(input('Digite o número: '))
            produto=produto*num
            i=i+1
        print(produto)
    elif escolha=='d':
        i=1
        soma=0
        produto=1
        while i<=15:
            num=int(input('Digite o número: '))
            if num%2==0:
                soma=soma+num
            else:
                produto=produto*num
            i=i+1
        print('A soma dos pares:',soma)
        print('O produto dos ímpares:',produto)
    elif escolha=='e':
        i=1
        feminino=0
        masculino=0
        while i<=10:
            sexo=input('Digite M para masculino ou F para feminino:')
            if sexo!='F' and sexo!='M':
                validade=False
                while validade==False:
                    print('Opção inválida')
                    sexo=input('Digite M para masculino ou F para feminino:')
                    if sexo=='F' or sexo=='M':
                        validade=True
            if sexo=='F':
                feminino=feminino+1
            else:
                masculino=masculino+1
            i=i+1
        print('Quantidade de Femininos:',feminino)
        print('Quantidade de masculino',masculino)
    elif escolha=='f':
        n=int(input('Digite a quantidade de idades a serem lidas: '))
        i=1
        maior=0
        menor=200
        while i<=n:
            idade=int(input('Digite a idade: '))
            if idade>maior:
                maior=idade
            if idade<menor:
                menor=idade
            i=i+1
        print('A maior idade foi:',maior)
        print('A menor idade foi:',menor)
    elif escolha=='g':
        n=int(input('Digite a quantidade de idades a serem lidas: '))
        i=1
        criancas=0
        adolescentes=0
        adultos=0
        idosos=0
        while i<=n:
            idade=int(input('Digite a idade: '))
            if idade<=11:
                criancas=criancas+1
            elif (idade>=12) and (idade<=18):
                adolescentes=adolescentes+1
            elif (idade>=19) and (idade<=60):
                adultos=adultos+1
            else:
                idosos=idosos+1
            i=i+1
        print('A quantidade de crianças:',criancas)
        print('A quantidade de adolescentes:',adolescentes)
        print('A quantidade de adultos:',adultos)
        print('A quantidade de idosos:',idosos)
    print('Escolha o que quer fazer de acordo com a tabela a seguir: \n')
    print('a.Calcular a soma de 15 números inteiros')
    print('b.Calcular a média de 10 números inteiros')
    print('c.Calcular o produto de 10 números inteiros')
    print('d.Ler 15 números, mostrar o produto dos ímpares e a soma dos pares')
    print('e.Ler o sexo de 10 pessoas e mostrar quantas são Masculinas e quantas são femininas')
    print('f.Ler a idade de N pessoas e mostrar a maior e a menor')
    print('g.Ler a idade de N pessoas e mostrar quantas são crianças, adolescentes, adultos e idodos')
    print('s.Sair')
    escolha=input(':')
print('Até mais!!!!')
    

