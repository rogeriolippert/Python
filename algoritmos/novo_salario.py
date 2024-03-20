'''
12. Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, 
desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final. 
'''
def calcula_novo_salario(salario):

    salario_aumento = (salario * 0.15) + salario
    aux = salario_aumento * 8/100
    novo_salario = salario_aumento - aux 


    return f"O seu salario inicial era de R${salario:.2f} após o aumento de 15% passou a ser de R${salario_aumento:.2f}, porem a um desconto de 8% que é retido para IR(imposto de renda). Sendo assim seu salario final fica no valor de R${novo_salario:.2f}"

def main():
    salario = float(input("Digite o valor do seu salario atual: "))
    print(calcula_novo_salario(salario))
main()  
