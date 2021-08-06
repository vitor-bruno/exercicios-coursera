def ordenada(lista):
    fim = len(lista)
    
    for i in range(1, fim):
        if lista[i] < lista[i-1]:
            return False
    return True