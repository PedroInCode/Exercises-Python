print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos vc quer mostrar? ')) #Lendo a quantidade de termos
t1 = 0 
t2 = 1 

print('-=' * 30)
print('{} -> {} '.format(t1, t2), end='') #mostrando os dois numeros iniciais.
cont = 3 #Ja temos 2 termos, t1 e t2! Entao o contador ja inicia no 3.

while cont <= n: #Equanto o contador for menor que a quantidade de termos:
    t3 = t1 + t2 #T3 e a soma de t1 e t2.
    print('-> {} '.format(t3), end='') #Mostrando o t3.
    cont += 1 #Ja temos 2 termos, 0 e 1! Se eu quiser 4 termos, ele so vai mostrar mais 2.
    t1 = t2 # O t1 passa a ser o t2
    t2 = t3 # O t2 passa a ser o t3
    # O t3 sempre vai ser a soma de t1 e t2.
print('-> Fim')