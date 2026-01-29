times = ('Santos','Corinthians','Palmeiras','São Paulo','Flamengo','Fluminense','Botafogo','Vasco','Gremio','Chapecoense', 'Cruzeiro')

print('-'*70)
print(f'Lista dos times do Brasileirão: {times}', end='')
print('-'*70)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-'*70)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-'*70)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*70)
for pos, time in enumerate(times):
    if time == 'Gremio':
        print(f'O {time} está na {pos}° posição no Brasileirão.')
        break
print('-'*70)