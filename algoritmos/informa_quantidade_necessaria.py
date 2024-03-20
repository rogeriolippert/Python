'''
16. A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de 
queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou 
presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em 
que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em 
quilos) de queijo, presunto e carne necessários para compra. 

'''

def carne_necessario(sanduiche):
    gramas_por_fatia_queijo = 0.05*2
    gramas_por_fatia_presunto = 0.1 
    gramas_por_rodela_hamburguer = 0.1

    quantidade_em_kilo_presunto = sanduiche * gramas_por_fatia_presunto
    quantidade_em_kilo_queijo = sanduiche * gramas_por_fatia_queijo
    quantidade_em_kilo_hamburguer = sanduiche * gramas_por_rodela_hamburguer

    print(f"{quantidade_em_kilo_hamburguer:.2f}Kg de Hamburguer")
    print(f"{quantidade_em_kilo_presunto:.2f}Kg de Presunto")
    print(f"{quantidade_em_kilo_queijo:.2f}Kg de Queijo")


def main ():

    sanduiche = float(input("Digite quantidade de sanduiches:"))
    return carne_necessario(sanduiche)


main()    