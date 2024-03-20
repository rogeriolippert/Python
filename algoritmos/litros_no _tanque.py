'''
#
# 5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o 
# preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no 
# tanque. 
#
'''

def litros_no_tanque(preco_gasolina, dinheiro_pago):

    litros_no_tanque = dinheiro_pago / preco_gasolina
    return litros_no_tanque

def main():
   
   preco_gasolina = float(input("Digíte o preço da gasolina por litro:"))
   dinheiro_pago = float(input("Digíte o valor pago em dinheiro:"))

   resultado = litros_no_tanque(preco_gasolina, dinheiro_pago)   

   print(f"A quantidade de litros no tanque é de {resultado}")
main()

