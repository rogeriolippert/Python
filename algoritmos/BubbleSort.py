#Ordenação de Lista (Bubble Sort):
#Objetivo: Implementar o algoritmo de ordenação Bubble Sort para ordenar uma lista de números.

def BubbleSort(lista):
    n = len(lista)

    for i in range(n):

        for j in range(0, n-i-1):

            if lista[j] > lista[j +1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
# Exemplo de uso:
minha_lista = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(minha_lista)

print("Lista ordenada:", minha_lista)





