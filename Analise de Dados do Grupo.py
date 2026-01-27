totalmais18 = homens = mulheresmenos20 = 0

while True:
    print('-'*40)
    print('CADASTRE UMA PESSOA ')
    print('-'*40)

    idade = int(input('Idade: '))
    if idade >= 18:
        totalmais18 += 1

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    cadastro = ' '
    while cadastro not in 'SsNn':
        print('-'*40)
        cadastro = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if cadastro == 'N':
        break

print('-'*40)
print(f'Total de pessoas com mais de 18 anos: {totalmais18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos.')

        