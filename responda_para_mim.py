from random import choice
respostas= ['Não','Hmm, acho melhor não', 'Sim', 'É uma boa ideia', 'Talvez', 'Com certeza', 'Pense bem antes de agir', 'É uma péssima escolha', 'Faça o que achar melhor', 'Não faça']
duvida=input('Tem alguma pergunta ? Se sim digite:Sim, senão digite:Não\n')
print('')
while (duvida=='Sim'):
    pergunta=input('Digite sua pergunta:\n')
    print('')
    resp = choice(respostas)
    print(resp)
    duvida=input('Mais alguma pergunta ? Se sim digite:Sim, senão digite:Não\n')
    print('')
print('Sem perguntas, tudo bem!!')
