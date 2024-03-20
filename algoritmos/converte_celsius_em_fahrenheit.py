'''
17. Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça um 
algoritmo para ler uma temperatura Celsius e imprimi-Ia em Fahrenheit (pesquise como fazer este 
tipo de conversão). 
'''

def converte_temperatura(c):
    F= (c*9/5)+32 
    print(f"A temperatura em °F {F:.2f}")
def main():
    c =float(input("Digite a sua temperatura em Celsius:"))
    return converte_temperatura(c)
main()