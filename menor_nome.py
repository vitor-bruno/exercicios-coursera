def menor_nome(nomes):
    menor = nomes[0].strip()
    for nome in nomes:
        if len(nome.strip()) < len(menor):
            menor = nome.strip()
    return menor.strip().capitalize()