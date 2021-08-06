def maior_elemento(lista):
    mv = lista[0]
    for n in lista:
        if n > mv:
            mv = n
    return mv