'''
9. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo 
vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a 
quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina 
informe quanto será o valor arrecadado. 
'''

def valor_arrecadado(quantidade, tamanho):   
# Dicionário que mapeia os tamanhos para os preços
    precos = {'P': 10, 'M': 12, 'G': 15}
    #Verifica se o tamanho informado é valido
    if tamanho in precos: 
        #Obtém preço correspondente ao tamanho informado
        preco_unitario = precos[tamanho]
        #calcula o Valor total arrecadado
        valor_arrecadado = quantidade * preco_unitario
        # Exibe o valor total arrecadado
        print(f"O valor arrecadado para {quantidade} peças tamanho {tamanho} é R${valor_arrecadado:.2f}")
    else:
        print("Tamanho inválido. Por favor, escolha entre P, M ou G.")
def main():    
    quantidade = int(input("Informa a quantidade de camisa: "))
    tamanho = str(input("Informe o tamanho [P, M ou G]: "))
    return valor_arrecadado(quantidade, tamanho)
main()
