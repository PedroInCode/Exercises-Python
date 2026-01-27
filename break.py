s = n = cont = 0

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Voce digitou {cont} numeros e a soma de todos eles vale {s}')