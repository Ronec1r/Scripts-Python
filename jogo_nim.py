def computador_escolhe_jogada(n,m):
    multiplo=(m+1)
    validade=False
    x=m
    while validade==False:
        if x>=1:
            if (((n-x)%multiplo)==0):
                validade=True
                return (x)
            else:
                x=x-1
        else:
            validade=True
            return(m)

def usuario_escolhe_jogada(n,m):
    jogada=int(input('Quantas peças você vai tirar? '))
    if (jogada>=1) and (jogada<=m):
        return jogada
    else:
        print('Oops! Jogada inválida! Tente de novo.')
        validacao=False
        while validacao==False:
            jogada=int(input())
            if (jogada>=1) and (jogada<=m):
                validacao=True
                return jogada

def partida():
    num_pecas=int(input('Quantas peças? '))
    num_jogadas=int(input('Limite de peças por jogada? '))
    if (num_jogadas>num_pecas):
        while (num_jogadas>num_pecas):
            print('O número de jogadas precisa ser menor que o número de peças!')
            num_jogadas=int(input('Limite de peças por jogada? '))
    if (num_pecas%(num_jogadas+1))==0:
        print('Você começa!')
        while num_pecas!=0:
            num_funcao=usuario_escolhe_jogada(num_pecas,num_jogadas)
            print('Você tirou',num_funcao,'peças.')
            num_pecas=num_pecas-num_funcao
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Você ganhou!')
                return 1
            computador_escolhe_jogada(num_pecas,num_jogadas)
            print('O computador tirou',computador_escolhe_jogada(num_pecas,num_jogadas),'peças.')
            num_pecas=num_pecas-(computador_escolhe_jogada(num_pecas,num_jogadas))
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Computador ganhou!')
                return 2
    else:
        print('Computador começa!')
        while num_pecas!=0:
            computador_escolhe_jogada(num_pecas,num_jogadas)
            print('O computador tirou',computador_escolhe_jogada(num_pecas,num_jogadas),'peças.')
            num_pecas=num_pecas-(computador_escolhe_jogada(num_pecas,num_jogadas))
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Computador ganhou!')
                return 2
            num_funcao=usuario_escolhe_jogada(num_pecas,num_jogadas)
            print('Você tirou',num_funcao,'peças.')
            num_pecas=num_pecas-num_funcao
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Você ganhou!')
                return 1

def campeonato():
    i=1
    j=0
    c=0
    while i<=3:
        print('**** Rodada',i,'****')
        decisao=partida()
        if decisao==1:
            j=j+1 
        elif decisao==2:
            c=c+1
        i=i+1
    print('**** Final do campeonato! ****') 
    print('Placar: Você',j,'X',c,'Computador')

print('Bem-vindo ao jogo do NIM! Escolha:')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato 2')
escolha=int(input(': '))
if (escolha<1) or (escolha>2):
    print('Opção Inválida, tente de novo!')
    validade_de_escolha=False
    while validade_de_escolha==False:
        print('Bem-vindo ao jogo do NIM! Escolha:')
        print('1 - para jogar uma partida isolada')
        print('2 - para jogar um campeonato 2')
        escolha=int(input(': '))
        if (escolha==1) or (escolha==2):
            validade_de_escolha=True
if escolha==1:
    partida()
elif escolha==2:
    campeonato()
