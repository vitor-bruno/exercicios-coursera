from math import sqrt

a = float(input('Coeficiente "a": '))
b = float(input('Coeficiente "b": '))
c = float(input('Coeficiente "c": '))

delta = b**2 - 4*a*c

if delta < 0:
    print('esta equação não possui raízes reais')
else:
    r1 = (-b + sqrt(delta)) / (2 * a)
    r2 = (-b - sqrt(delta)) / (2 * a)
    if delta == 0:
        print(f'a raiz desta equação é {r1}')
    else:
        if r1 < r2:
            print(f'as raízes da equação são {r1} e {r2}')
        else:
            print(f'as raízes da equação são {r2} e {r1}')
