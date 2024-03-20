'''
7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do 
ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias. 

'''

def calcula_dias(dia, mes):
    
    resultado = dia + (mes*30)
    return resultado 

def main():
    dia = int(input("Digíte o dia: "))
    mes = int(input("Digíte o Mês: "))

    tempo_inicio_ano = calcula_dias(dia, mes)

    print(f"Ja se passaram {tempo_inicio_ano} dias do ano")


main()
