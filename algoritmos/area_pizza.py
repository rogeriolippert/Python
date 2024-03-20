'''
14. Calcule a área de uma pizza que possui um raio R (pi=3.14)

'''
def calcular_area(pizza):

    area = pizza*(3.14**2)

    print(f"Area de sua pizza é de {area:.2f}")
def main():
    pizza = float(input("Digíte a circunferência da sua pizza:"))

    return calcular_area(pizza)
    
main()