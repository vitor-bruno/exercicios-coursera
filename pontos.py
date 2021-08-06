from math import sqrt
x1 = float(input('Coordenada x do ponto 1: '))
y1 = float(input('Coordenada y do ponto 1: '))
x2 = float(input('Coordenada x do ponto 2: '))
y2 = float(input('Coordenada y do ponto 2: '))
d = sqrt((x1 - x2)**2 + (y1 - y2)**2)

if d >= 10:
    print('longe')
else:
    print('perto')