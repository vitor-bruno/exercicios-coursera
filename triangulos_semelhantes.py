class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        lista1 = sorted([self.a, self.b, self.c])
        lista2 = sorted([triangulo.a, triangulo.b, triangulo.c])
        if (lista1[0]/lista2[0]) == (lista1[1]/lista2[1]) == (lista1[2]/lista2[2]):
            return True
        else:
            return False