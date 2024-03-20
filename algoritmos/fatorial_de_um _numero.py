import math

def main():
    # Solicitar um número ao usuário
    numero_usuario = int(input("Digite um número para calcular o fatorial: "))

    # Verificar se o número é não-negativo
    if numero_usuario < 0:
        print("Por favor, digite um número não-negativo.")
        return

    # Calcular e imprimir o fatorial usando a função math.factorial
    resultado_fatorial = math.factorial(numero_usuario)
    print(f"O fatorial de {numero_usuario} é {resultado_fatorial}.")

if __name__ == "__main__":
    main()
