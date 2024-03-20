'''
# 1. A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as 
# dimensões de um terreno e depois exibir a área do terreno.
# 
'''
import math
def area_do_terreno(x, y):
    area = x * y
    return area

def main(terreno):
    
#Exemplo de uso
    x = 13.75
    y = 15.80
#
    resultado = area_do_terreno(x, y)

#
    print("Area do terreno é ",resultado)
main(None)
