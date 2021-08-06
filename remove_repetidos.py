def remove_repetidos(lista):
    lista.sort()
    lista2 = []
    for n in lista:
        if n not in lista2:
            lista2.append(n)
    return lista2