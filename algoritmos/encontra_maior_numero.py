'''
#
# Maior Número em uma Lista:Objetivo: Encontrar o maior número em uma lista de números fornecida.
#
'''
def encontrar_maior_numero(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

# Exemplo de uso
numeros = [10, 5, 7, 243, 2, 20]
maior_numero = encontrar_maior_numero(numeros)

if maior_numero is not None:
    print(f"O maior número na lista é: {maior_numero}")
else:
    print("A lista está vazia.")
