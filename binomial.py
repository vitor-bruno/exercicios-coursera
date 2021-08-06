def fatorial(n):
    if n < 0:
        return 0
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


def binomial(n, k):
    b = fatorial(n)/(fatorial(k)*fatorial(n-k))
    return int(b)


print(binomial(5, 3))
print(binomial(4, 1))
print(binomial(6, 6))
print(binomial(3, 0))
print(binomial(20, 10))