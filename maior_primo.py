def éPrimo(k):
    c = 2
    primo = True
    while primo and c < k:
        if k % c == 0:
            return False
        c += 1
    if primo:
        return True


def maior_primo(n):
    for c in range(n, 1, -1):
        if éPrimo(c):
            return c