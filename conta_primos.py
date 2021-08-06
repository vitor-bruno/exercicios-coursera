def primo(x):
    primo = True
    c = 2
    while primo and c < x:
        if x % c == 0:
            primo = False
        c += 1
    return primo


def n_primos(n):
    c = 0
    while n >= 2:
        if primo(n):
            c += 1
        n -= 1
    return c