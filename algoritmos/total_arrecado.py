'''
3. A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a 
cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber 
quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de 
poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com 
base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular 
os dados solicitados.

'''
import math

def poupanca(x, y):
    paozinho = 0.12
    broa = 1.50
    total_arrecado = 0.10

    resultado = (x * paozinho + y * broa) * total_arrecado
    return resultado

def main():
    x = float(input("Quantidade pãozinho: "))
    y = float(input("Quantidade broa: "))

    resultado_final = poupanca(x, y)
    print("O resultado é:", resultado_final)

# Chame a função main sem argumentos
main()

