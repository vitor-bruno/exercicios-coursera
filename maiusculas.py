def maiusculas(frase):
    mai = ''
    for letra in frase:
        if 65 <= ord(letra) <= 90:
            mai += letra
    return mai