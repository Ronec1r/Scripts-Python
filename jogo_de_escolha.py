print('Você acorda em um corredor escuro...\n')
print('Um assassino está atrás de você...\n')
print('Tente sair daí sem encontrar ele\n')
print('Tem quatros portas que você pode escolher:\n')
print('|                |\n')
print('|                |\n')
print('|                |\n')
print('3                4\n')
print('|                |\n')
print('|                |\n')
print('|                |\n')
print('1                2\n')
print('|                |\n')
print('|                |\n')
porta=int(input('Escolha entre uma das portas\n'))
def validade(entrada,i,j):
    if (entrada<i) or (entrada>j):
        validade=False 
        while validade==False:
            print('Não existe essa porta, escolha outra\n')
            entrada=int(input('Escolha entre uma das portas\n'))
            if (entrada<i) or (entrada>j):
                validade=False
            else:
                validade=True
validade(porta,1,4)
if porta==1:
    print('O assassino te pegou, Fim de Jogo!!')
elif porta==2:
    print('Uma sala sem saída, o assassino te trancou nela e você morreu sem ar!!')
elif porta==3:
    print('Você entrou numa sala com mais duas portas:\n')
    print('|----------------|\n')
    print('5                6\n')
    print('|                |\n')
    print('|______________  |\n')
    porta=int(input('Escolha entre uma das portas\n'))
    validade(porta,5,6)
    if porta==5:
        print('O assassino te pegou, Fim de jogo!!')
    else:
        resposta_sala_6=input('Aqui possui uma janela aberta, deseja pular? Se deseja digite Sim\n')
        if (resposta_sala_6=='Sim'):
            print('A janela era muito alta, você quebrou o pescoço e morreu, Fim de jogo!!')
        else:
            print('Você decidiu não pular e o assassino te achou, Fim de jogo!!')
else:
    print('Você entrou numa sala com uma porta:\n')
    print('|----------------|\n')
    print('7                |\n')
    print('|                |\n')
    print('|______________  |\n')
    resposta_da_sala_7=input('Deseja entra nela?, Se deseja digite Sim\n')
    if (resposta_da_sala_7=='Sim'):
        print('Parabéns, você conseguiu escapar!!')
    else:
        print('Você decidiu não entrar e o assassino te pegou, Fim de jogo!!')

