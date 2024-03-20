'''
8. Faça um algoritmo para ler três notas de um aluno em uma disciplina e imprimir a sua média 
ponderada (as notas tem pesos respectivos de 1, 2 e 3). 

'''

def media_podenrada(n1, n2, n3):
    ponderada = (((n1*0.1)+(n2*0.2)+(n3*0.3)) / (0.1 + 0.2 + 0.3))
    return ponderada

def main(): 
    n1= float(input("Digite a sua primira  nota: "))
    n2= float(input("Digite a sua segunda  nota: "))
    n3= float(input("Digite a sua terceira nota: "))


    resultado = media_podenrada(n1, n2, n3)
    print(f"A sua média ponderada ficou {resultado:.2f}")
main()