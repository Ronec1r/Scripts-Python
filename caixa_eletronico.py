print('Escoha o que fazer de acordo com o menu a seguir: ')
print('1.Consultar saldo de caixa eletrônico')
print('2.Sacar')
print('9.Sair')
escolha=int(input(': '))
dinheiro_no_caixa=940
nota_cem=5
nota_cinquenta=5
nota_vinte=5
nota_dez=5
nota_cinco=5
nota_dois=5
nota_um=5
while escolha!=9:
    if escolha==1:
        print('Saldo no caixa:',dinheiro_no_caixa,'R$')
    elif escolha==2:
        qt_cem=0
        qt_cinquenta=0
        qt_vinte=0
        qt_dez=0
        qt_cinco=0
        qt_dois=0
        qt_um=0
        saque=int(input('Digite o valor a ser sacado: '))
        if saque>dinheiro_no_caixa:
            while saque>dinheiro_no_caixa:
                print('Dinheiro no caixa indisponível para esse saque!!')
                saque=int(input('Digite o valor a ser sacado: '))
        dinheiro_no_caixa=dinheiro_no_caixa-saque
        while saque>0:
            if nota_cem>=1 and saque>=100:
                saque=saque-100
                qt_cem=qt_cem+1
                nota_cem=nota_cem-1
            elif nota_cinquenta>=1 and saque>=50:
                saque=saque-50
                qt_cinquenta=qt_cinquenta+1
                nota_cinquenta=nota_cinquenta-1
            elif nota_vinte>=1 and saque>=20:
                saque=saque-20
                qt_vinte=qt_vinte+1
                nota_vinte=nota_vinte-1
            elif nota_dez>=1 and saque>=10:
                saque=saque-10
                qt_dez=qt_dez+1
                nota_dez=nota_dez-1
            elif nota_cinco>=1 and saque>=5:
                saque=saque-5
                qt_cinco=qt_cinco+1
                nota_cinco=nota_cinco-1
            elif nota_dois>=1 and saque>=2:
                saque=saque-2
                qt_dois=qt_dois+1
                nota_dois=nota_dois-1
            elif nota_um>=1 and saque>=1:
                saque=saque-1
                qt_um=qt_um+1
                nota_um=nota_um-1    
        print('Saque efetuado com sucesso!!')
        print('Notas usadas para saque:\n100:',qt_cem,'\n50:',qt_cinquenta,'\n20:',qt_vinte,'\n10:',qt_dez,'\n5:',qt_cinco,'\n2:',qt_dois,'\n1:',qt_um)
    print('Escoha o que fazer de acordo com o menu a seguir: ')
    print('1.Consultar saldo de caixa eletrônico')
    print('2.Sacar')
    print('9.Sair')
    escolha=int(input(': '))
print('Até mais!!!')
    
