'''
#  
# 2. Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.
#
'''
import math

def ferraduras_necessarias(qtdCavalos):
    ferraduras = qtdCavalos * 4

    return ferraduras

def main(cavalos):
# Exemplo uso
    qtdCavalos = 128
    resultado = ferraduras_necessarias(qtdCavalos)
    print("São necessárias", resultado)

main(None)