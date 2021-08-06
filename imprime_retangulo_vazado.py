larg = int(input('Digite a largura: '))
alt = int(input('Digite a altura: '))
c = 0

while alt > 0:
    if c == 0 or alt == 1:
        print('#' * larg)
    else:
        print('#' + (' ' * (larg - 2) + '#'))
    alt -= 1
    c += 1
