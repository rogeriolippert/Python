'''
# A função abs(x) em Python retorna o valor absoluto de x, ou seja, a distância de x até zero, 
# sem considerar a direção. Em termos simples, ela retorna o valor numérico sem sinal.

# Aqui está um exemplo de uso:
# No exemplo de uso 01, abs(numero) retorna 10, que é a distância de -10 até zero, 
# sem levar em conta a direção negativa.
# Você pode usar a função abs() com qualquer tipo de número em Python, 
# incluindo inteiros e números de ponto flutuante. Como usando o exemplo 02:
# Neste caso, abs(numero_float) retorna 3.14.
# A função abs() é útil em situações onde você quer garantir que um valor seja tratado como positivo, 
# independentemente do seu sinal original.
#
'''
#Exemplo de uso  01
numero = -10
valor_absoluto = abs(numero)

print(f"O valor absoluto de {numero} é {valor_absoluto}")

#Exemplo de uso 02
numero_float = -3.14
valor_absoluto_float = abs(numero_float)

print(f"O valor absoluto de {numero_float} é {valor_absoluto_float}")

