'''
11. Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. Faça um 
algoritmo para converter este tempo em anos, meses e dias. Assuma que cada mês possui sempre 
30 dias

'''

def converter_dias_para_anos_meses_dias(dias_totais):
    dias = dias_totais
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    dias_por_ano = 365

    # calcular o número de anos
    anos = dias // 365
    dias_restantes = dias % 365

    # calcular o número de meses e dias restantes
    meses = 0
    for i, dias_mes in enumerate(dias_por_mes):
        if dias_restantes >= dias_mes:
            meses += 1
            dias_restantes -= dias_mes
        else:
            break

    # retornar o resultado fora do loop
    return f"{dias_totais} dias correspondem a {anos} anos, {meses} meses e {dias_restantes} dias."

def main():
    dias_totais = int(input("Informe a quantidade de dias sem acidentes na empresa: "))
    print(converter_dias_para_anos_meses_dias(dias_totais))

main()

      