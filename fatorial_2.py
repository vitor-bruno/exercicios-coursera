def fatorial(n):
    m = n - 1
    while m > 0:
        n *= m
        m -= 1
    if n == 0:
        n = 1
    return n

n = int(input('Digite um número inteiro: '))
while n > 0:
    print(f'O fatorial de {n} é {fatorial(n)}\n')
    n = int(input('Digite outro número inteiro: '))
