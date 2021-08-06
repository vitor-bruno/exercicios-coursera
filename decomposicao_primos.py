n = int(input('Digite um número inteiro maior que 1: '))
fator = 2
contagem = 0
print(f'{n} = ', end='')
while n > 1:
    while n % fator == 0:
        print(f'{fator} x ', end='') if n // fator != 1 else print(f'{fator}', end='')
        n /= fator
        contagem += 1
    fator += 1
    contagem = 0