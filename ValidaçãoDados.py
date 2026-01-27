#Exercício 1 - Validação de Dados
sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))