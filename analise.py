media = 0
soma = 0
maioridadeM = 0
nomevelho = ''
totalM20 = 0

for c in range(1, 5):
    print('----- {} Pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maioridadeM = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeM:
        maioridadeM = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalM20 += 1


media = soma / 4
print('------------------')
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos de idade.'.format(maioridadeM))
print('Ao todo são {} melheres com menos de 20 anos.'.format(totalM20))
