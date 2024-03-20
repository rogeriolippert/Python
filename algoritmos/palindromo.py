'''
Verificação de Palíndromo:
-Objetivo: Verificar se uma palavra ou frase é um palíndromo (lê-se da mesma forma de trás para frente).
'''
def verifica_palindromo(texto):
    #Remove espaços em brancos e torne todas as letras minúsculas para evitar discrepâncias
    texto = texto.replace(" ","").lower()

    #Campare a string original com sua inversa
    return texto == texto[::-1]

#Exemplos de uso 

palavra ="radar"
frase ="Anotaram a data  da maratona"

print(f"A palavra '{palavra}' é uma palíndromo?{verifica_palindromo(palavra)}")
print(f"A palavra '{frase}' é uma palíndromo?{verifica_palindromo(frase)}")
