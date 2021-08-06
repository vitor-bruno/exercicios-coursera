import random
import time


class Ordenador:
    def ordenada(self, lista):
        fim = len(lista)
        
        for i in range(1, fim):
            if lista[i] < lista[i-1]:
                return False
        return True

    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            min = i

            for j in range(i+1, fim):
                if lista[j] < lista[min]:
                    min = j
            
            lista[i], lista[min] = lista[min], lista[i]

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            if self.ordenada(lista):
                break


class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print('Bolha demorou', depois - antes, 'segundos')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Seleção direta demorou', depois - antes, 'segundos')

