n = int(input('Digite um número inteiro: '))
anterior = n % 10
n = n // 10
possui_adjacentes = False

while not possui_adjacentes and n != 0:
    ultimo = n % 10
    if ultimo == anterior:
        possui_adjacentes = True
    n = n // 10
    anterior = ultimo

if possui_adjacentes:
    print('sim')
else:
    print('não')