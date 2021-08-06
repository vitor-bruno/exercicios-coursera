n = int(input('Digite um número inteiro: '))
s = 0
while n != 0:
    v = n // (10 ** (len(str(n)) - 1))
    n = n % (10 ** (len(str(n)) - 1))
    s += v
print(s)