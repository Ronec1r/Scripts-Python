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
    if (jogada>=1) and (jogada<=m) and (jogada<=n):
        return jogada
    else:
        print('Oops! Jogada inválida! Tente de novo.')
        validacao=False
        while validacao==False:
            jogada=int(input('Quantas peças você vai tirar? '))
            if (jogada>=1) and (jogada<=m):
                validacao=True
                return jogada

def partida():
    num_pecas=int(input('Quantas peças? '))
    num_jogadas=int(input('Limite de peças por jogada? '))
    if (num_jogadas>=num_pecas):
        while (num_jogadas>=num_pecas):
            print('O número de jogadas precisa ser menor que o número de peças!')
            num_jogadas=int(input('Limite de peças por jogada? '))
    if (num_pecas%(num_jogadas+1))==0:
        print('Você começa!')
        while num_pecas!=0:
            armego=usuario_escolhe_jogada(num_pecas,num_jogadas)
            print('Você tirou',armego,'peças.')
            num_pecas=num_pecas-armego
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Você ganhou!')
                breakpoint
            computador_escolhe_jogada(num_pecas,num_jogadas)
            print('O computador tirou',computador_escolhe_jogada(num_pecas,num_jogadas),'peças.')
            num_pecas=num_pecas-(computador_escolhe_jogada(num_pecas,num_jogadas))
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Computador ganhou!')
                breakpoint
    else:
        print('Computador começa!')
        while num_pecas!=0:
            computador_escolhe_jogada(num_pecas,num_jogadas)
            num_pecas=num_pecas-(computador_escolhe_jogada(num_pecas,num_jogadas))
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Computador ganhou!')
                j=j+1
                breakpoint
            armego=usuario_escolhe_jogada(num_pecas,num_jogadas)
            num_pecas=num_pecas-armego
            print('Agora restam',num_pecas,'no tabuleiro.')
            if num_pecas==0:
                print('Fim do jogo! Você ganhou!')
                c=c+1
                breakpoint




partida()