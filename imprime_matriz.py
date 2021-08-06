def imprime_matriz(matriz):
    for c in range(len(matriz)):
        for cc in range(len(matriz[c])):
            if cc < len(matriz[c])-1:
                print(f'{matriz[c][cc]} ', end='')
            else:
                print(matriz[c][cc])
