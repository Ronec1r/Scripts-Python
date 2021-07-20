codigo=int(input('Digite o código do curso: '))
curso=input('Digite o nome do curso: ')
num_vagas=int(input('Digite o número de vagas do curso: '))
num_fem=int(input('Digite o número de candidatos do sexo feminino: '))
num_mas=int(input('Digite o número de candidatos do sexo masculino: '))
candidatos=num_fem+num_mas
if num_vagas<30:
    while num_vagas<30:
        print('Número de vagas precisa ser de pelo menos 30!')
        num_vagas=int(input('Digite o número de vagas do curso: '))
if candidatos<=0:
    while candidatos<=0:
        print('Número de candidatos precisa ser maior que zero!')
        num_fem=int(input('Digite o número de candidatos do sexo feminino: '))
        num_mas=int(input('Digite o número de candidatos do sexo masculino: '))
        candidatos=num_fem+num_mas
maior_qt=0
maior_codigo=0
maior_curso=''
total_candidatos=0
while codigo!=0:
    total_candidatos=total_candidatos+candidatos
    pe_fem=(num_fem*100)/candidatos
    pe_mas=(num_mas*100)/candidatos
    print('O curso',curso,'tem',num_vagas,'vagas para',candidatos,'candidatos, onde',pe_fem,'são mulheres e',pe_mas,'são homens!!')
    print('')
    if candidatos>maior_qt:
        maior_qt=candidatos
        maior_codigo=codigo
        maior_curso=curso
    codigo=int(input('Digite o código do curso: '))
    curso=input('Digite o nome do curso: ')
    num_vagas=int(input('Digite o número de vagas do curso: '))
    num_fem=int(input('Digite o número de candidatos do sexo feminino: '))
    num_mas=int(input('Digite o número de candidatos do sexo masculino: '))
    candidatos=num_fem+num_mas
    if num_vagas<30:
        while num_vagas<30:
            print('Número de vagas precisa ser de pelo menos 30!')
            num_vagas=int(input('Digite o número de vagas do curso: '))
    if candidatos<=0:
        while candidatos<=0:
            print('Número de candidatos precisa ser maior que zero!')
            num_fem=int(input('Digite o número de candidatos do sexo feminino: '))
            num_mas=int(input('Digite o número de candidatos do sexo masculino: '))
            candidatos=num_fem+num_mas
print('')
print('O número total de candidatos no processo seletivo foi:',total_candidatos)
print('')
print('O maior número de candidatos foi',maior_qt,'no curso',maior_curso,'com código',maior_codigo,'!!')
    


