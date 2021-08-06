def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        lin = len(m1)
        col = len(m1[0])
        mat = []
        for l in range(lin):
            linha = []
            for c in range(col):
                linha.append(m1[l][c]+m2[l][c])
            mat.append(linha)
        return mat
    else:
        return False
