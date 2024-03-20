'''
10. Construa um algoritmo para calcular a distância entre dois pontos do plano cartesiano. Cada 
ponto é um par ordenado (x,y).
'''

import math 

def calcular_distancia_entre_pontos(pontoA_x, pontoA_y, pontoB_x, pontoB_y ):
    # Calculando a diferença entre as coordenadas x e y dos pontos A e B
    diferenca_x = pontoB_x - pontoA_x
    diferenca_y = pontoB_y - pontoA_y
    # Calculando a distância entre os pontos A e B usando a fórmula da distância euclidiana
    distancia = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)
    # Exibindo o resultado
    print(f"A distância entre os pontos A e B é: {distancia:.2f}")
def main():
    # Entrada do usuário para as coordenadas dos pontos A e B
    pontoA_x, pontoA_y = map(float, input("Digite as coordenadas do ponto A (x y): ").split())
    pontoB_x, pontoB_y = map(float, input("Digite as coordenadas do ponto B (x y): ").split())
    # Chamando a função para calcular a distância entre os pontos A e B
    return calcular_distancia_entre_pontos(pontoA_x, pontoA_y, pontoB_x, pontoB_y)
main()

