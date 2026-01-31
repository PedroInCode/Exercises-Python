valores = [] #Criando uma lista vazia.
for cont in range(0,6): #Lendo 6 números e adicionando eles na lista (valores).
    num = int(input('Digite um valor: '))
    valores.append(num) #Adicionando o valor a lista.
for c, v in enumerate(valores): #Para cada posição, elemento in valores.
    print(f'Na posição {c} encontrei o valor {v}.') #Mostrando o elemento e sua posição na lista.

print('-'*50)

a = [2, 3, 4, 7]
#b = a -> Desta forma as duas listas ficam interligadas!! Sendo impossível de alterar algum valor em somente 1 lista. 
b = a[:] #Essa maneira faz com que o b receba todos os valores de a sem causar ligação entre as listas. Sendo possível alterar algum valor tanto da lista a ou b.
b[2] = 8 #Alterando o elemento da lista b que está na posição 2, que é o 4. Ele vai passar a ser 8.
print(f'Lista A: {a}')
print(f'Lista B: {b}')