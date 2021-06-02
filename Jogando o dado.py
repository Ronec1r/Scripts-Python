import random

n=input('Você quer jogar o dado ? Responda com Sim ou Não\n')

if (n=='Sim') or (n=='sim'):
    sinal=True
    while (sinal==True) :
        dado=random.randint(1,6)
        print('O número sorteado foi: ',dado)
        n=input('Você quer jogar o dado ? Responda com Sim ou Não\n')
        if (n!='Sim') and (n!='sim'):
            sinal=False
            print('Tudo bem !!')    
else :
    print('Tudo bem!!')
