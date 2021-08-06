from math import sqrt


def bhaskara_delta(a, b, c):
    return b**2 - 4*a*c


def bhaskara_raizes(a, b, c):
    d = bhaskara_delta(a, b, c)
    if bhaskara_delta(a, b, c) < 0:
        print('esta equação não possui raízes reais')
    else:
        r1 = (-b + sqrt(d)) / (2 * a)
        r2 = (-b - sqrt(d)) / (2 * a)
        if d == 0:
            print(f'a raiz desta equação é {r1}')
        else:
            if r1 < r2:
                print(f'as raízes da equação são {r1} e {r2}')
            else:
                print(f'as raízes da equação são {r2} e {r1}')


def bhaskara():
    a = float(input('Coeficiente "a": '))
    b = float(input('Coeficiente "b": '))
    c = float(input('Coeficiente "c": '))
    bhaskara_raizes(a, b, c)