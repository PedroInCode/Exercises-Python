
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = 0

while opcao != 5:
    print('''    [ 1 ] Somar 
    [ 2 ] Multiplicar 
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opcao = int(input('>>>>>>>Qual é a sua Opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é igual a {}.'.format(n1, n2, soma))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    if opcao == 2:
        multiplicação = n1 * n2
        print('A Multiplicação dos dois números é igual a {}.'.format(multiplicação))
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    if opcao == 3:
        if n1 > n2:
            print('O número {} é MAIOR.'.format(n1))
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        elif n2 > n1:
            print('O número {} é MAIOR.'.format(n2))
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        else:
            print('Os números {} e {} são IGUAIS.'.format(n1, n2))
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
    if opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

print('Fim do Programa.')
         