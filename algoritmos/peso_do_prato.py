'''
6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo 
que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a 
balança já desconte o peso do prato. 

'''
def quilo_de_refeicao(peso_do_prato):
    
    tara = 0.400
    resultado = (peso_do_prato - tara) * 12  
    return resultado
def main():
    peso_do_prato=float(input("Digite o peso do prato:"))

    imprimi_valor_pagar = quilo_de_refeicao(peso_do_prato)

    print(f"O valor a pagar {imprimi_valor_pagar:.2f}")
main()