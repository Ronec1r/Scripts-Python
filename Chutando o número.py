import random
num_sorteado=random.randint(1,10)
num_chutado=int(input('Chute um número entre 1 e 10!\n'))
acerto=False
while (acerto!=True) :
    if (num_chutado==num_sorteado) :
        print('Parabéns, você acertou!!!')
        acerto=True
    elif (num_chutado>num_sorteado) :
        print('O número chutado é maior que o número sorteado\n')
        num_chutado=int(input('Chute um número entre 1 e 10!\n'))
    else :
        print('O número chutado é menor que o número sorteado\n')
        num_chutado=int(input('Chute um número entre 1 e 10!\n'))

