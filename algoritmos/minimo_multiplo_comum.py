'''
#
# Mínimo Múltiplo Comum (MMC): Objetivo: Calcular o Mínimo Múltiplo Comum
# de dois números.
#
'''
import math
def decompor_em_fatores_primos(numeros):
    fatores_primos = []
    divisor = 2
    
    while numeros > 1:
        while numeros % divisor == 0:
            fatores_primos.append(divisor)
            numeros //= divisor
        divisor += 1
    return fatores_primos

def calcular_mmc(a, b):
    fatores_primos_a = decompor_em_fatores_primos(a)
    fatores_primos_b = decompor_em_fatores_primos(b)

    fatores_comuns = []
    fatores_nao_comuns_a = fatores_primos_a.copy()

    for fator in fatores_primos_b:
        if fator in fatores_nao_comuns_a:
            fatores_nao_comuns_a.remove(fator)
            fatores_comuns.append(fator)
    mmc = 1

    for fator in fatores_primos_a + fatores_primos_b:
        mmc *= fator
    return mmc

#Exemplo de uso

numero1 = 15
numero2 = 67

resultado = calcular_mmc(numero1, numero2)

print(f"O MMC de {numero1} e {numero2} é {resultado}")


