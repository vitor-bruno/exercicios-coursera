def é_hipotenusa(x, c1, c2):
    if (x ** 2) == (c1 ** 2) + (c2 ** 2):
        return True
    else:
        return False


def soma_hipotenusas(n):
    c = 1
    soma = 0
    while c <= n:     
        a = 1
        b = 1
        while a < n:
            while b < n:
                if é_hipotenusa(c, a, b):
                    soma += c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1   
    return soma
