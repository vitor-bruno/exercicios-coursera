numeros = []
n = int(input('Digite um número: '))

while n > 0:
    numeros.insert(0, n)
    n = int(input('Digite um número: '))

for n in numeros:
    print(n)