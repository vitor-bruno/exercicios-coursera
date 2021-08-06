def maximo(a, b, c):
    if c <= a >= b:
        return a
    if c <= b >= a:
        return b
    if a <= c >= b:
        return c