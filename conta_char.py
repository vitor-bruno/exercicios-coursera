def conta_letras(frase, contar='vogais'):
    vog = con = ''
    frase = frase.lower().replace(' ','')
    assert contar == 'vogais' or 'consoantes'
    for letra in frase:
        if letra in 'aeiou':
            vog += letra
        else:
            con += letra
    if contar == 'vogais':
        return len(vog)
    else:
        return len(con)