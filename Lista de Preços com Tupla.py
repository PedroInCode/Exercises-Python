listagem = ('Lápis', 1.75,
            'Borrecha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90
            )
print('-'*40)
print(f'{'Listagem de Preços':^40}') # :^40 - Colocando o Titulo centralizado dentro da mesma quantidade das linhas a cima e abaixo. 
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') #:.<30 Ajusta para a esquerda num espaço de 30 caracteres colocando pontos nos espaços que estão vazios.
    else:
        print(f'R${listagem[pos]:>1.2f}') #.2f Serve para colocar em duas casas decimais. ex: 25 -> 25.00 
print('-'*40)
                                        