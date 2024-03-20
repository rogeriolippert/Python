'''
#
# Sequência de Fibonacci: Objetivo: Gerar os primeiros n termos da Sequência de Fibonacci.
#
'''
def fibonacci(n):
    
    termo1, termo2 = 0, 1
    sequencia = [termo1, termo2]

    for _ in range(2, n):
        proximo_termo = termo1 + termo2
        sequencia.append(proximo_termo)

        termo1, termo2 = termo2, proximo_termo 
    return sequencia
# Solicita ao usuário a quantidade de termos desejada
n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

# Chama a função e imprime os termos gerados
resultado = fibonacci(n)
print(resultado)