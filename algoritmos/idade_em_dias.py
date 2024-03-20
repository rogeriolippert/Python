'''
#
# 4. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida 
# ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa 
# com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 
# DIAS
#
'''

def quantos_dias_de_vida(idade):

    idade *=  365
    return idade
def main( ):

    name = str(input("Dígite o seu nome:")) 
    idade = int(input("Dígite a sua idade:"))

    resultado = quantos_dias_de_vida(idade)

    print(f"{name}VOCÊ JÁ VIVEU",resultado)

main()

    