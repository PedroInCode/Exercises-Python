#Estrutura de Repetição

n1 = int(input('Digite um número: '))
for c in range(0, n1+1):
    print(c)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
print('FIM')

s = 0
for c in range(0, 3):
    n = int(input('Digite um Valor: '))
    s += n
print('O Total foi de {}'.format(s))
print('FIM')
