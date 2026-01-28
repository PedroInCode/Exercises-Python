lanche = ('Agua', 'Suco', 'Refrigerante', 'Energético')
#print(lanche[0:1])

#Tuplas são Imutáveis.
# lanche[1] = 'pizza' -> Vai dar erro! Não é possível fazer alterações.

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('---------------------------------------------------------------------------')

for pos, comida in enumerate(lanche): # Serve para mostrar a comida e sua posição dentro da variável composta.
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print('-'*40)

print(sorted(lanche)) #Organiza em ordem alfabética.

print('-'*40)

a = (2, 5, 4)
b = (5, 8, 1, 2)
#Criando uma terceira Tupla para armazenar o que tem nas outras duas.
c = b + a #Obs: A ordem altera o resultado.
print(c) #mostra as duas Tuplas juntas
print(len(c)) #Mostra a quantidade de elementos dentro da Tupla.
print(c.count(5)) #Quantas vezes o 5 aparece dentro da Tupla c?
print(c.index(2)) #Em que posição está o 5?