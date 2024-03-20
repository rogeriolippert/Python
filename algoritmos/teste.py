def calcular_ingredientes_sanduiche(numero_sanduiches):
    # Define o peso de cada ingrediente em gramas
    peso_queijo = 50  # gramas
    peso_presunto = 50  # gramas
    peso_hamburguer = 100  # gramas

    # Calcula o peso total de cada ingrediente necessário
    peso_total_queijo = 2 * peso_queijo * numero_sanduiches
    peso_total_presunto = peso_presunto * numero_sanduiches
    peso_total_hamburguer = peso_hamburguer * numero_sanduiches

    # Converte os pesos para quilogramas
    peso_total_queijo_kg = peso_total_queijo / 1000
    peso_total_presunto_kg = peso_total_presunto / 1000
    peso_total_hamburguer_kg = peso_total_hamburguer / 1000

    return peso_total_queijo_kg, peso_total_presunto_kg, peso_total_hamburguer_kg

# Solicita a quantidade de sanduíches ao usuário
quantidade_sanduiches = int(input("Quantidade de sanduíches a fazer: "))

# Calcula a quantidade de ingredientes necessários
queijo_kg, presunto_kg, hamburguer_kg = calcular_ingredientes_sanduiche(quantidade_sanduiches)

# Exibe os resultados
print(f"Quantidade de queijo necessária: {queijo_kg:.2f} kg")
print(f"Quantidade de presunto necessária: {presunto_kg:.2f} kg")
print(f"Quantidade de hambúrguer necessária: {hamburguer_kg:.2f} kg")
