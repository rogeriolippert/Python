'''
13. Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma: 
CENTENA = x 
DEZENA = x 
UNIDADE = x 

'''
def imprimir_digitos(centena, dezena, unidade):
    print("CENTENA =", centena)
    print("DEZENA  =", dezena)
    print("UNIDADE =", unidade)

def converte_numero_intero(numero):
    # Verificar se o número tem até três dígitos
    if 0 <= numero <= 999:  
        CENTENA = numero // 100
        DEZENA = (numero % 100) // 10
        UNIDADE = numero % 10
        imprimir_digitos(CENTENA, DEZENA, UNIDADE)
    else:
        print("O número deve ter até três dígitos.")

def main():
    numero = int(input("Digite um número inteiro (assuma até três dígitos): "))
    converte_numero_intero(numero)

main()
