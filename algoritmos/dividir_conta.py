'''15. Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar. Faça um 
algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que 
Carlos e André não paguem centavos. Ex: uma conta de R$101,53 resulta em R$33,00 para 
Carlos, R$33,00 para André e R$35,53 para Felipe.

'''
def dividir_conta(valor_total):
    # Divide o valor total por 3 para obter a parte igual de cada amigo
    parte_igual = valor_total / 3
    
    # Calcula quanto Carlos e André devem pagar (arredondando para baixo para o número inteiro mais próximo)
    carlos_e_andre = int(parte_igual)
    
    # O que sobra depois de tirar a parte de Carlos e André é o que Felipe deve pagar
    felipe = valor_total - 2 * carlos_e_andre
    
    # Retorna o valor que cada amigo deve pagar
    return carlos_e_andre, carlos_e_andre, felipe

def main():
    # Solicita ao usuário o valor total da conta
    valor_total = float(input("Digite o valor total da conta: R$ "))
    
    # Chama a função para dividir a conta
    carlos, andre, felipe = dividir_conta(valor_total)
    
    # Exibe quanto cada amigo deve pagar
    print(f"Carlos deve pagar: R$ {carlos:.2f}")
    print(f"André deve pagar: R$ {andre:.2f}")
    print(f"Felipe deve pagar: R$ {felipe:.2f}")

# Chama a função principal
main()

