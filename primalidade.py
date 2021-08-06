def primo(x):
    primo = True
    c = 2
    while primo and c < x:
        if x % c == 0:
            primo = False
        c += 1
    return primo

n = int(input('Digite um número inteiro (0 para sair): '))
while n > 0:
    if primo(n):
        print(f'{n} é um número primo\n')
    else:
        print(f'{n} não é um número primo\n')
    n = int(input('Digite outro número inteiro (0 para sair): '))
