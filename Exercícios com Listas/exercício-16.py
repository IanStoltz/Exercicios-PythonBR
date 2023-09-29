""" 
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por
semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana
recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine
quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299; $300 - $399; $400 - $499; $500 - $599; $600 - $699; $700 - $799; $800 - $899; $900 - $999; $1000 em diante
"""

salarios = []
contadores = [0] * 8
limites_intervalos = [299, 399, 499, 599, 699, 799, 899, 999]
intervalos = [
    "$200 - $299",
    "$300 - $399",
    "$400 - $499",
    "$500 - $599",
    "$600 - $699",
    "$700 - $799",
    "$800 - $899",
    "$900 - $999",
    "$1000 em diante",
]
# Coletando número de vendedores
num_vendedores = int(input("Quantos vendedores a loja tem? "))

# Coletando salários de cada vendedor
for vendedor in range(1, num_vendedores + 1):
    vendas = float(input(f"\nQuanto o vendedor {vendedor} arrecadou essa semana? "))
    salario = vendas + 200 + ((vendas * 9) / 100)
    salarios.append(salario)

print(f"Os salários são: {salarios}")

# Associando os salários conforme faixa salarial
for salario in salarios:
    for i, limite in enumerate(limites_intervalos):
        if salario <= limite:
            contadores[i] += 1
            break

# Associando salários na faixa acima de 1000
contadores.append(sum(1 for salario in salarios if salario >= 1000))

# Mostrando os intervalos e a quantia de vendedores em cada um
for i in range(len(contadores)):
    print(
        f"Número de vendedores com salário no intervalo {intervalos[i]}: {contadores[i]}"
    )
