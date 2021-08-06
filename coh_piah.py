import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("\nBem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a sua assinatura.'''
    palavras = []
    tam_frases = []
    tam_palavras = []
    tam_sentencas = []
    
    for sentenca in separa_sentencas(texto):
        tam_sentencas.append(len(sentenca))
        for frase in separa_frases(sentenca):
            tam_frases.append(len(frase))
            for palavra in separa_palavras(frase):
                tam_palavras.append(len(palavra))
                palavras.append(palavra)
    
    wal = sum(tam_palavras) / len(tam_palavras)
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    hlr = n_palavras_unicas(palavras) / len(palavras)
    sal = sum(tam_sentencas) / len(tam_sentencas)
    sac = len(tam_frases) / len(tam_sentencas)
    pal = sum(tam_frases) / len(tam_frases)

    return [wal, ttr, hlr, sal, sac, pal]

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(len(as_a)):
        soma += (abs(as_a[i] - as_b[i]))
    return soma / 6

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e devolve o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []
    for texto in textos:
        similaridades.append(compara_assinatura(calcula_assinatura(texto), ass_cp))
    return similaridades.index(min(similaridades)) + 1