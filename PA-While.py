print('-=' * 15)
print('        Gerador de PA        ')
print('-=' * 15)

primeiro = int(input('Digite o primeiro Termo: '))
razão = int(input('Digite a Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos no total.'.format(total))